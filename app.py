import streamlit as st

from wordGenerator import gerar_docx
from constants import DADOS_BANCARIOS_ELEANDRO, DADOS_BANCARIOS_NORONHA
from extractors import (
    read_uploaded_file,
    extract_from_promad,
    extract_from_pje,
    detect_petition_type,
)
from templates import (
    dados_bancarios_noronha,
    dados_bancarios_parceria,
    dados_eletronicos_noronha,
    dados_eletronicos_parceria,
    dados_bancarios_eletronicos_noronha,
    dados_bancarios_eletronicos_parceria,
    juizo_100_digital_noronha,
    juizo_100_digital_parceria,
    juizo_100_digital_com_dados_noronha,
    juizo_100_digital_com_dados_parceria,
    desinteresse_conciliacao_noronha,
    desinteresse_conciliacao_parceria,
    interesse_conciliacao_noronha,
    interesse_conciliacao_parceria,
    interesse_audiencia_conciliacao_noronha,
    interesse_audiencia_conciliacao_parceria,
    impugnacao_calculos_noronha,
    impugnacao_calculos_parceria,
    concordancia_calculos_noronha,          # ← NOVO
    concordancia_calculos_parceria,         # ← NOVO
    juntada_documentos_noronha,
    juntada_documentos_parceria,
    cumprimento_intimacao_noronha,
    cumprimento_intimacao_parceria,
    audiencia_telepresencial_noronha,
    audiencia_telepresencial_parceria,
    manifestacao_simples_noronha,
    manifestacao_simples_parceria,
    juntada_calculos_noronha,
    juntada_calculos_parceria,
    pedido_generico_noronha,
    pedido_generico_parceria,
)

st.set_page_config(page_title="Petições | ES & MF", layout="centered")
st.title("⚖️ Gerador de Petições")

# ── MODELO ────────────────────────────────────────────────────────────────────

modelo = st.radio(
    "Modelo do escritório",
    ["Parceria Marília + Eleandro", "Noronha"],
    horizontal=True,
)

st.divider()

# ── SESSION STATE ─────────────────────────────────────────────────────────────

_DEFAULTS = {
    "f_processo":   "",
    "f_vara":       "",
    "f_comarca":    "Porto Alegre",
    "f_reclamante": "",
    "f_reclamado":  "",
    "f_id":         "",
    "tipo_sugerido": None,
    "promad_nome":   None,
    "pje_nome":      None,
    "ocr_debug_promad": "",
    "ocr_debug_pje":    "",
}

for _k, _v in _DEFAULTS.items():
    if _k not in st.session_state:
        st.session_state[_k] = _v

# ── UPLOADS ───────────────────────────────────────────────────────────────────

st.subheader("📎 Envie os prints")

col_u1, col_u2 = st.columns(2)

with col_u1:
    st.markdown("📋 **Print do PROMAD**")
    st.caption("Extrai: processo · partes · vara · comarca · tipo")
    promad_file = st.file_uploader(
        "promad",
        type=["png", "jpg", "jpeg", "pdf"],
        key="upload_promad",
        label_visibility="collapsed",
    )

with col_u2:
    st.markdown("**⚖️ Print do PJe**")
    st.caption("Extrai: ID do despacho / intimação")
    pje_file = st.file_uploader(
        "pje",
        type=["png", "jpg", "jpeg", "pdf"],
        key="upload_pje",
        label_visibility="collapsed",
    )

# ── PROCESSA PROMAD ───────────────────────────────────────────────────────────

if promad_file and promad_file.name != st.session_state.promad_nome:
    with st.spinner("🔍 Lendo PROMAD..."):
        try:
            texto_bruto = read_uploaded_file(promad_file)
            st.session_state.ocr_debug_promad = texto_bruto
            if not texto_bruto.strip():
                st.warning("⚠️ OCR não encontrou texto na imagem do PROMAD. Verifique se o Tesseract está instalado.")
            else:
                dados = extract_from_promad(texto_bruto)
                if dados.get("processo"):    st.session_state.f_processo   = dados["processo"]
                if dados.get("vara"):        st.session_state.f_vara       = dados["vara"]
                if dados.get("comarca"):     st.session_state.f_comarca    = dados["comarca"]
                if dados.get("reclamante"):  st.session_state.f_reclamante = dados["reclamante"]
                if dados.get("reclamado"):   st.session_state.f_reclamado  = dados["reclamado"]
                tipo_det = detect_petition_type(
                    dados.get("titulo", ""),
                    dados.get("agendamento", ""),
                )
                if tipo_det:
                    st.session_state.tipo_sugerido = tipo_det
                st.session_state.promad_nome = promad_file.name
                campos_achados = [k for k in ["processo", "vara", "comarca", "reclamante", "reclamado"] if dados.get(k)]
                if campos_achados:
                    st.success(f"✅ PROMAD lido! Campos extraídos: {', '.join(campos_achados)}")
                else:
                    st.warning("⚠️ PROMAD lido, mas nenhum campo foi identificado. Veja o texto extraído abaixo.")
        except Exception as e:
            st.error(f"❌ Erro ao processar PROMAD: {e}")

# ── PROCESSA PJe ──────────────────────────────────────────────────────────────

if pje_file and pje_file.name != st.session_state.pje_nome:
    with st.spinner("🔍 Lendo PJe..."):
        try:
            texto_bruto = read_uploaded_file(pje_file)
            st.session_state.ocr_debug_pje = texto_bruto
            if not texto_bruto.strip():
                st.warning("⚠️ OCR não encontrou texto na imagem do PJe. Verifique se o Tesseract está instalado.")
            else:
                dados = extract_from_pje(texto_bruto)
                if dados.get("id_despacho"):
                    st.session_state.f_id = dados["id_despacho"]
                if dados.get("processo")   and not st.session_state.f_processo:
                    st.session_state.f_processo   = dados["processo"]
                if dados.get("reclamante") and not st.session_state.f_reclamante:
                    st.session_state.f_reclamante = dados["reclamante"]
                if dados.get("reclamado")  and not st.session_state.f_reclamado:
                    st.session_state.f_reclamado  = dados["reclamado"]
                st.session_state.pje_nome = pje_file.name
                id_msg = st.session_state.f_id or "não encontrado"
                st.success(f"✅ PJe lido! ID extraído: **{id_msg}**")
        except Exception as e:
            st.error(f"❌ Erro ao processar PJe: {e}")

# ── DEBUG ─────────────────────────────────────────────────────────────────────

with st.expander("🔬 Ver texto extraído pelo OCR (diagnóstico)"):
    st.markdown("**PROMAD:**")
    st.text(st.session_state.ocr_debug_promad or "(nenhum texto ainda)")
    st.markdown("**PJe:**")
    st.text(st.session_state.ocr_debug_pje or "(nenhum texto ainda)")

st.divider()

# ── DADOS DO PROCESSO ─────────────────────────────────────────────────────────

st.subheader("📋 Dados do processo")
st.caption("Confira os dados extraídos e corrija se necessário.")

col1, col2 = st.columns(2)

with col1:
    st.text_input("Número do processo *", key="f_processo",  placeholder="0001234-56.2024.5.04.0001")
    st.text_input("Vara",                 key="f_vara",       placeholder="Ex: 10ª Vara do Trabalho")
    st.text_input("Comarca",              key="f_comarca",    placeholder="Porto Alegre")

with col2:
    st.text_input("Reclamante *",         key="f_reclamante", placeholder="Nome completo")
    st.text_input("Reclamado *",          key="f_reclamado",  placeholder="Nome ou razão social")

processo   = st.session_state.f_processo
vara       = st.session_state.f_vara
comarca    = st.session_state.f_comarca
reclamante = st.session_state.f_reclamante
reclamado  = st.session_state.f_reclamado

st.divider()

# ── TIPO DE PETIÇÃO ───────────────────────────────────────────────────────────

st.subheader("📝 Tipo de petição")

TIPOS_VALIDOS = [
    "Dados bancários",
    "Dados eletrônicos",
    "Dados bancários + eletrônicos",
    "Juízo 100% Digital",
    "Juízo 100% Digital + Dados eletrônicos",
    "Audiência telepresencial",
    "Juntada de documentos",
    "Juntada de cálculos",
    "Impugnação aos cálculos",
    "Concordância com os cálculos",          # ← NOVO
    "Cumprimento de intimação",
    "Manifestação simples",
    "Desinteresse em conciliação",
    "Interesse em conciliação",
    "Interesse em audiência de conciliação",
    "Pedido genérico",
]

tipo_idx = 0
if st.session_state.tipo_sugerido in TIPOS_VALIDOS:
    tipo_idx = TIPOS_VALIDOS.index(st.session_state.tipo_sugerido)
    st.info(f"🧠 Tipo identificado pelo PROMAD: **{st.session_state.tipo_sugerido}**")

tipo = st.selectbox("Selecione ou confirme o tipo", TIPOS_VALIDOS, index=tipo_idx)

st.divider()

# ── CAMPOS EXTRAS ─────────────────────────────────────────────────────────────

st.subheader("✏️ Informações complementares")

id_despacho         = ""
texto_livre         = ""
aceita_digital      = True
titular             = ""
cpf_cnpj            = ""
banco               = ""
agencia             = ""
conta               = ""
reclamante_telefone = ""
reclamante_email    = ""

TIPOS_COM_ID = [
    "Dados eletrônicos",
    "Dados bancários + eletrônicos",
    "Juízo 100% Digital",
    "Juízo 100% Digital + Dados eletrônicos",
    "Desinteresse em conciliação",
    "Juntada de documentos",
    "Juntada de cálculos",
    "Impugnação aos cálculos",
    "Concordância com os cálculos",          # ← NOVO
    "Interesse em audiência de conciliação",
    "Cumprimento de intimação",
    "Audiência telepresencial",
    "Manifestação simples",
]

if tipo in TIPOS_COM_ID:
    id_despacho = st.text_input(
        "ID do despacho / intimação",
        key="f_id",
        placeholder="Ex: e304b77",
    )

if tipo in ["Dados bancários", "Dados bancários + eletrônicos"]:
    dados_banco = (
        DADOS_BANCARIOS_ELEANDRO
        if modelo == "Parceria Marília + Eleandro"
        else DADOS_BANCARIOS_NORONHA
    )
    st.markdown("🏦 **Dados bancários**")
    col1, col2 = st.columns(2)
    with col1:
        titular  = st.text_input("Titular",  value=dados_banco.get("titular", ""))
        cpf_cnpj = st.text_input("CNPJ/CPF", value=dados_banco.get("cpf_cnpj", ""))
        banco    = st.text_input("Banco",     value=dados_banco.get("banco", ""))
    with col2:
        agencia = st.text_input("Agência", value=dados_banco.get("agencia", ""))
        conta   = st.text_input("Conta",   value=dados_banco.get("conta", ""))

TIPOS_COM_CONTATO = [
    "Dados eletrônicos",
    "Dados bancários + eletrônicos",
    "Juízo 100% Digital + Dados eletrônicos",
]

if tipo in TIPOS_COM_CONTATO:
    st.markdown("📱 **Contato do reclamante**")
    col1, col2 = st.columns(2)
    with col1:
        reclamante_telefone = st.text_input("Telefone", placeholder="51 99999-9999")
    with col2:
        reclamante_email = st.text_input("E-mail", placeholder="email@gmail.com")

if tipo == "Juízo 100% Digital":
    opcao = st.radio("Posição", ["✅ Aceita o Juízo 100% Digital", "❌ Não aceita"], horizontal=True)
    aceita_digital = opcao.startswith("✅")

TIPOS_TEXTO_LIVRE = [
    "Juntada de documentos",
    "Juntada de cálculos",
    "Cumprimento de intimação",
    "Audiência telepresencial",
    "Manifestação simples",
    "Pedido genérico",
]

if tipo in TIPOS_TEXTO_LIVRE:
    labels = {
        "Juntada de documentos":    "Descreva os documentos juntados",
        "Juntada de cálculos":      "Observações (opcional)",
        "Cumprimento de intimação": "Descreva o cumprimento",
        "Audiência telepresencial": "Motivo do pedido",
        "Manifestação simples":     "Texto da manifestação",
        "Pedido genérico":          "Descreva o pedido",
    }
    texto_livre = st.text_area(labels.get(tipo, "Texto"), placeholder="Digite aqui...", height=130)

if tipo in (
    "Interesse em conciliação",
    "Interesse em audiência de conciliação",
    "Impugnação aos cálculos",
    "Concordância com os cálculos",
):
    st.info("ℹ️ Nenhuma informação complementar adicional necessária.")

st.divider()

# ── GERAR ─────────────────────────────────────────────────────────────────────

if st.button("⚙️ Gerar Petição", type="primary", use_container_width=True):
    erros = []
    if not processo.strip():   erros.append("Número do processo")
    if not reclamante.strip(): erros.append("Reclamante")
    if not reclamado.strip():  erros.append("Reclamado")
    if erros:
        st.error(f"❌ Preencha os campos obrigatórios: {', '.join(erros)}")
        st.stop()

    try:
        noronha = modelo == "Noronha"
        args = dict(vara=vara, comarca=comarca, processo=processo,
                    reclamante=reclamante, reclamado=reclamado)

        if tipo == "Dados bancários":
            fn = dados_bancarios_noronha if noronha else dados_bancarios_parceria
            gerado = fn(**args, titular=titular, cpf_cnpj=cpf_cnpj, banco=banco, agencia=agencia, conta=conta)

        elif tipo == "Dados eletrônicos":
            fn = dados_eletronicos_noronha if noronha else dados_eletronicos_parceria
            gerado = fn(**args, id_despacho=id_despacho, reclamante_telefone=reclamante_telefone, reclamante_email=reclamante_email)

        elif tipo == "Dados bancários + eletrônicos":
            fn = dados_bancarios_eletronicos_noronha if noronha else dados_bancarios_eletronicos_parceria
            gerado = fn(**args, titular=titular, cpf_cnpj=cpf_cnpj, banco=banco, agencia=agencia, conta=conta,
                        id_despacho=id_despacho, reclamante_telefone=reclamante_telefone, reclamante_email=reclamante_email)

        elif tipo == "Juízo 100% Digital":
            fn = juizo_100_digital_noronha if noronha else juizo_100_digital_parceria
            gerado = fn(**args, id_despacho=id_despacho, aceita=aceita_digital)

        elif tipo == "Juízo 100% Digital + Dados eletrônicos":
            fn = juizo_100_digital_com_dados_noronha if noronha else juizo_100_digital_com_dados_parceria
            gerado = fn(**args, id_despacho=id_despacho, reclamante_telefone=reclamante_telefone, reclamante_email=reclamante_email)

        elif tipo == "Desinteresse em conciliação":
            fn = desinteresse_conciliacao_noronha if noronha else desinteresse_conciliacao_parceria
            gerado = fn(**args, id_despacho=id_despacho)

        elif tipo == "Interesse em conciliação":
            fn = interesse_conciliacao_noronha if noronha else interesse_conciliacao_parceria
            gerado = fn(processo=processo, reclamante=reclamante, reclamado=reclamado)

        elif tipo == "Interesse em audiência de conciliação":
            fn = interesse_audiencia_conciliacao_noronha if noronha else interesse_audiencia_conciliacao_parceria
            gerado = fn(**args, id_despacho=id_despacho)

        elif tipo == "Impugnação aos cálculos":
            fn = impugnacao_calculos_noronha if noronha else impugnacao_calculos_parceria
            gerado = fn(**args, id_despacho=id_despacho)

        elif tipo == "Concordância com os cálculos":         # ← NOVO
            fn = concordancia_calculos_noronha if noronha else concordancia_calculos_parceria
            gerado = fn(**args, id_despacho=id_despacho)

        elif tipo == "Juntada de documentos":
            fn = juntada_documentos_noronha if noronha else juntada_documentos_parceria
            gerado = fn(**args, id_despacho=id_despacho, descricao=texto_livre)

        elif tipo == "Juntada de cálculos":
            fn = juntada_calculos_noronha if noronha else juntada_calculos_parceria
            gerado = fn(**args, id_despacho=id_despacho, descricao=texto_livre)

        elif tipo == "Cumprimento de intimação":
            fn = cumprimento_intimacao_noronha if noronha else cumprimento_intimacao_parceria
            gerado = fn(**args, id_despacho=id_despacho, descricao=texto_livre)

        elif tipo == "Audiência telepresencial":
            fn = audiencia_telepresencial_noronha if noronha else audiencia_telepresencial_parceria
            gerado = fn(**args, id_despacho=id_despacho, motivo=texto_livre)

        elif tipo == "Manifestação simples":
            fn = manifestacao_simples_noronha if noronha else manifestacao_simples_parceria
            gerado = fn(**args, id_despacho=id_despacho, texto=texto_livre)

        elif tipo == "Pedido genérico":
            fn = pedido_generico_noronha if noronha else pedido_generico_parceria
            gerado = fn(**args, texto=texto_livre)

        else:
            st.error("Tipo não reconhecido.")
            st.stop()

        nome = "peticao.docx"
        gerar_docx(gerado, modelo=modelo, nome_arquivo=nome)

        with open(nome, "rb") as f:
            st.download_button(
                label="📥 Baixar petição (.docx)",
                data=f,
                file_name=f"peticao_{tipo.lower().replace(' ', '_').replace('+', 'e')}.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                use_container_width=True,
            )

        st.success("✅ Petição gerada com sucesso!")

        with st.expander("👁️ Pré-visualizar texto"):
            st.text(gerado)

    except Exception as e:
        st.error(f"❌ Erro ao gerar petição: {e}")
        raise e