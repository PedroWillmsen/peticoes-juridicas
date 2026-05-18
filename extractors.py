import io
import re
import platform

import pytesseract
from PIL import Image
from pypdf import PdfReader

if platform.system() == "Windows":
    pytesseract.pytesseract.tesseract_cmd = (
        r'C:\Users\Comercial19\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    )

try:
    from pdf2image import convert_from_bytes
except Exception:
    convert_from_bytes = None


# ── LEITURA DE ARQUIVO ────────────────────────────────────────────────────────

def read_uploaded_file(uploaded_file) -> str:
    content = uploaded_file.read()
    ext = uploaded_file.name.lower().split(".")[-1]
    if ext == "pdf":
        return _read_pdf(content)
    return _read_image_bytes(content)


def _read_pdf(content: bytes) -> str:
    try:
        reader = PdfReader(io.BytesIO(content))
        texto  = "\n".join(p.extract_text() or "" for p in reader.pages).strip()
        if len(texto) > 50:
            return texto
    except Exception:
        pass
    if convert_from_bytes:
        try:
            imagens = convert_from_bytes(content)
            return "\n".join(
                pytesseract.image_to_string(img, lang="por+eng")
                for img in imagens
            ).strip()
        except Exception:
            pass
    return ""


def _read_image_bytes(content: bytes) -> str:
    try:
        img = Image.open(io.BytesIO(content))
        return pytesseract.image_to_string(img, lang="por+eng").strip()
    except Exception:
        return ""


# ── LIMPEZA DE NOMES ──────────────────────────────────────────────────────────

_PREFIXOS_PARTE = [
    "CLIENTE", "AUTOR", "AUTORA", "RECLAMANTE", "RECLAMADO",
    "EXEQUENTE", "EXECUTADO", "REQUERENTE", "REQUERIDO",
    "IMPETRANTE", "IMPETRADO",
]


def _clean_name(nome: str) -> str:
    nome = re.sub(r'[^\w\sÀ-ÿ.,-]', ' ', nome)
    nome = re.sub(r'\s+', ' ', nome).strip().upper()
    for prefixo in _PREFIXOS_PARTE:
        if nome.startswith(prefixo + " "):
            nome = nome[len(prefixo):].strip()
            break
    nome = re.sub(r'^X\s+', '', nome).strip()
    return nome


# ── EXTRAÇÃO DO PROMAD ────────────────────────────────────────────────────────

def extract_from_promad(texto: str) -> dict:
    dados = {
        "processo":    "",
        "vara":        "",
        "comarca":     "Porto Alegre",
        "reclamante":  "",
        "reclamado":   "",
        "titulo":      "",
        "agendamento": "",
    }

    linhas = [l.strip() for l in texto.splitlines() if l.strip()]
    texto_full = " ".join(linhas)

    for linha in linhas:
        m = re.match(r'T[ií]tulo[:\s]+(.+)', linha, re.IGNORECASE)
        if m:
            dados["titulo"] = m.group(1).strip()
            break

    for linha in linhas:
        m = re.match(r'Agendamento[:\s]+(.+)', linha, re.IGNORECASE)
        if m:
            dados["agendamento"] = m.group(1).strip()
            break

    if not dados["titulo"] and linhas:
        dados["titulo"] = linhas[0]
    if not dados["agendamento"]:
        dados["agendamento"] = texto_full[:300]

    for linha in linhas:
        if not dados["processo"]:
            m = re.search(r'\b(\d{7}-\d{2}[.\-]\d{4}[.\-]\d[.\-]\d{2}[.\-]\d{4})\b', linha)
            if m:
                dados["processo"] = m.group(1)

    for linha in linhas:
        if not dados["vara"]:
            m = re.search(
                r'(\d+[ªºa-z°.\-]*\s*Vara\s+do\s+Trabalho[^,\n]*)',
                linha, re.IGNORECASE,
            )
            if m:
                dados["vara"] = _clean_vara(m.group(1).strip())

    if not dados["vara"]:
        for linha in linhas:
            m = re.match(r'Local de tr[âa]mite[:\s]+(.+)', linha, re.IGNORECASE)
            if m:
                dados["vara"] = _clean_vara(m.group(1).strip())
                break

    for linha in linhas:
        m = re.match(r'Comarca[:\s]+([A-ZÀ-Úa-zà-ú\s]+)', linha, re.IGNORECASE)
        if m:
            dados["comarca"] = m.group(1).strip()
            break

    for linha in linhas:
        m = re.match(r'Cliente[:\s]+(.+)', linha, re.IGNORECASE)
        if m:
            val = m.group(1).strip()
            partes = re.split(r'\s+[Xx]\s+', val, maxsplit=1)
            if len(partes) == 2:
                dados["reclamante"] = _clean_name(partes[0])
                dados["reclamado"]  = _clean_name(partes[1])
            else:
                dados["reclamante"] = _clean_name(val)
            break

    if not dados["reclamante"]:
        for linha in linhas:
            if re.search(r'\s[Xx]\s', linha):
                partes = re.split(r'\s+[Xx]\s+', linha, maxsplit=1)
                if len(partes) == 2 and partes[0].strip() and partes[1].strip():
                    dados["reclamante"] = _clean_name(partes[0])
                    dados["reclamado"]  = _clean_name(partes[1])
                    break

    if not dados["reclamante"]:
        for i, linha in enumerate(linhas):
            if linha.strip().upper() in ("X", "VS", "V.S.", "VERSUS"):
                if i > 0:
                    dados["reclamante"] = _clean_name(linhas[i - 1])
                if i < len(linhas) - 1:
                    dados["reclamado"]  = _clean_name(linhas[i + 1])
                break

    return dados


def _clean_vara(vara: str) -> str:
    vara = re.sub(r'[°º][-º°]', 'ª', vara)
    vara = re.sub(r'(\d+)[°º]', r'\1ª', vara)
    vara = re.sub(r'\s+', ' ', vara)
    return vara.strip()


# ── EXTRAÇÃO DO PJe ───────────────────────────────────────────────────────────

def extract_from_pje(texto: str) -> dict:
    dados = {
        "id_despacho": "",
        "processo":    "",
        "reclamante":  "",
        "reclamado":   "",
    }

    linhas = [l.strip() for l in texto.splitlines() if l.strip()]

    for linha in linhas:
        if not dados["processo"]:
            m = re.search(r'\b(\d{7}-\d{2}[.\-]\d{4}[.\-]\d[.\-]\d{2}[.\-]\d{4})\b', linha)
            if m:
                dados["processo"] = m.group(1)

    for linha in linhas:
        if dados["id_despacho"]:
            break

        m = re.search(r'\b[IlÍ][dD]\.?\s+([a-fA-F0-9]{5,12})\b', linha)
        if m:
            dados["id_despacho"] = m.group(1)
            continue

        m = re.search(r'\b([a-fA-F0-9]{6,10})\s*[-–]\s*[A-ZÁÉÍÓÚ]{2,}', linha)
        if m:
            candidato = m.group(1)
            if re.search(r'[a-fA-F]', candidato):
                dados["id_despacho"] = candidato
                continue

        m = re.search(r'\b(\d{6,12})\b', linha)
        if m:
            candidato = m.group(1)
            if dados["processo"] and candidato in dados["processo"].replace("-", "").replace(".", ""):
                continue
            dados["id_despacho"] = candidato
            continue

        m = re.search(r'[Nn]úmero do documento[:\s]+(\S+)', linha)
        if m:
            dados["id_despacho"] = m.group(1)

    for linha in linhas:
        if not dados["reclamante"] and re.search(r'\s[Xx]\s', linha):
            partes = re.split(r'\s+[Xx]\s+', linha, maxsplit=1)
            if len(partes) == 2:
                dados["reclamante"] = _clean_name(partes[0])
                dados["reclamado"]  = _clean_name(partes[1])

    return dados


# ── DETECÇÃO DO TIPO DE PETIÇÃO ───────────────────────────────────────────────

_TIPOS_ORDEM = [
    "Concordância com os cálculos",              # ← antes de Impugnação para evitar conflito
    "Impugnação aos cálculos",
    "Interesse em audiência de conciliação",
    "Interesse em conciliação",
    "Desinteresse em conciliação",
    "Audiência telepresencial",
    "Dados bancários + eletrônicos",
    "Dados bancários",
    "Dados eletrônicos",
    "Juízo 100% Digital",
    "Juntada de cálculos",
    "Juntada de documentos",
    "Cumprimento de intimação",
    "Manifestação simples",
    "Pedido genérico",
]

_KEYWORDS: dict[str, list[list[str]]] = {
    "Concordância com os cálculos": [
        ["concordar", "calculos"],
        ["concordancia", "calculos"],
        ["nao impugna", "calculos"],
        ["nao impugnar", "calculos"],
        ["concorda", "calculos"],
        ["homologacao", "calculos", "reclamada"],
    ],
    "Impugnação aos cálculos": [
        ["impugnacao calculos"],
        ["impugnacao", "calculos pc"],
        ["impugnacao", "calculos"],
        ["calculos pc"],
    ],
    "Interesse em audiência de conciliação": [
        ["interesse aud concil"],
        ["interesse", "aud", "concil"],
        ["interesse", "audiencia", "conciliacao", "telepresencial"],
        ["interesse", "audiencia", "zoom"],
        ["aud concil"],
    ],
    "Interesse em conciliação": [
        ["interesse em conciliar"],
        ["interesse", "cejusc"],
        ["pzo 5dd"],
        ["possui interesse", "conciliar"],
        ["remessa", "cejusc"],
    ],
    "Desinteresse em conciliação": [
        ["desinteresse em conciliar"],
        ["desinteresse em conciliacao"],
        ["desinteresse", "conciliar"],
        ["desinteresse", "conciliacao"],
        ["desinteresse", "audiencia"],
        ["desinteresse"],
        ["pzo", "conciliar"],
        ["pzo 10dd"],
        ["cjsg"],
        ["cjsm"],
        ["nao possui interesse", "conciliar"],
        ["nao possui interesse"],
    ],
    "Audiência telepresencial": [
        ["telepresencial"],
        ["videoconferencia"],
        ["audiencia", "video"],
        ["audiencia", "remota"],
    ],
    "Dados bancários + eletrônicos": [
        ["dados bancarios", "eletronicos"],
        ["bancarios", "eletronicos"],
    ],
    "Dados bancários": [
        ["conta bancaria", "pagamento"],
        ["deposito judicial"],
        ["informar conta bancaria"],
        ["dados bancarios", "fins de pagamento"],
    ],
    "Dados eletrônicos": [
        ["dados eletronicos"],
        ["endereco eletronico"],
        ["contato eletronico"],
    ],
    "Juízo 100% Digital": [
        ["juizo digital"],
        ["100% digital"],
        ["opcao", "digital"],
    ],
    "Juntada de cálculos": [
        ["calculos de liquidacao"],
        ["planilha de calculos"],
        ["juntada de calculos"],
        ["apresentar calculos"],
        ["homologacao de calculos"],
        ["liquidacao de sentenca"],
    ],
    "Juntada de documentos": [
        ["juntada de documentos"],
        ["juntar documentos"],
        ["apresentar documentos"],
    ],
    "Cumprimento de intimação": [
        ["cumprimento de intimacao"],
        ["cumprir intimacao"],
        ["em cumprimento", "intimacao"],
    ],
    "Manifestação simples": [
        ["manifestacao"],
        ["se manifestar"],
    ],
    "Pedido genérico": [
        ["requerimento"],
        ["requerer"],
    ],
}


def detect_petition_type(titulo: str, agendamento: str = "") -> str | None:
    texto = (titulo + " " + agendamento).lower()
    texto = (texto
             .replace("ç", "c").replace("ã", "a").replace("ê", "e")
             .replace("á", "a").replace("é", "e").replace("í", "i")
             .replace("ó", "o").replace("ú", "u").replace("â", "a"))

    for tipo in _TIPOS_ORDEM:
        grupos = _KEYWORDS.get(tipo, [])
        for grupo in grupos:
            grupo_norm = [
                kw.lower()
                   .replace("ç", "c").replace("ã", "a").replace("ê", "e")
                   .replace("á", "a").replace("é", "e").replace("í", "i")
                   .replace("ó", "o").replace("ú", "u").replace("â", "a")
                for kw in grupo
            ]
            if all(kw in texto for kw in grupo_norm):
                return tipo

    return None