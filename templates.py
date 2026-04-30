from datetime import date

from constants import DADOS_ELETRONICOS_ADVOGADOS


def _ano() -> int:
    return date.today().year


def format_juizo(vara: str, comarca: str) -> str:
    return f"{vara.upper()} DE {comarca.upper()}/RS"


# ══════════════════════════════════════════════════
# DADOS BANCÁRIOS
# ══════════════════════════════════════════════════

def dados_bancarios_noronha(
    vara, comarca, processo, reclamante, reclamado,
    titular, cpf_cnpj, banco, agencia, conta,
):
    return f"""EXCELENTÍSSIMO(A) SENHOR(A) JUIZ(A) DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{reclamante.upper()}**, por seus advogados signatários, vem, respeitosamente, à Douta e Elevada presença de Vossa Excelência, nos autos da reclamatória trabalhista que move em face de **{reclamado.upper()}**, expor e requerer o que adiante segue:

Tendo em vista a intimação para apresentação de dados bancários, a parte autora vem informar os seguintes dados para fins de liberação de valores:

Titular: {titular}
CNPJ/CPF: {cpf_cnpj}
Banco: {banco}
Agência: {agencia}
Conta: {conta}

Diante do exposto, requer que os dados bancários acima informados sejam cadastrados para fins de pagamento.

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


def dados_bancarios_parceria(
    vara, comarca, processo, reclamante, reclamado,
    titular, cpf_cnpj, banco, agencia, conta,
):
    return f"""AO JUÍZO DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{reclamante.upper()}**, já qualificado nos autos da reclamatória trabalhista promovida em face de **{reclamado.upper()}**, também já qualificado, vem, respeitosamente, à presença de Vossa Excelência, por meio de seus procuradores, dizer e requerer o que segue:

Tendo em vista a necessidade de informação de dados bancários para fins de liberação de valores, o exequente informa os dados bancários de seu procurador, com poderes para tanto, para transferência eletrônica:

Titular: {titular}
CNPJ/CPF: {cpf_cnpj}
Banco: {banco}
Agência: {agencia}
Conta Corrente: {conta}

Nestes termos, pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


# ══════════════════════════════════════════════════
# DADOS ELETRÔNICOS
# ══════════════════════════════════════════════════

def dados_eletronicos_noronha(
    vara, comarca, processo, reclamante, reclamado,
    id_despacho, reclamante_telefone, reclamante_email,
):
    adv = DADOS_ELETRONICOS_ADVOGADOS
    intro = f"em atenção à decisão de ID {id_despacho}, " if id_despacho.strip() else ""

    return f"""EXCELENTÍSSIMO(A) SENHOR(A) JUIZ(A) DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{reclamante.upper()}**, por seus advogados signatários, vem, respeitosamente, à Douta e Elevada presença de Vossa Excelência, nos autos da reclamatória trabalhista que move em face de **{reclamado.upper()}**, {intro}informar os dados eletrônicos seus e de seus procuradores, conforme abaixo:

Procuradores:

{adv["marilia_nome"]}
Telefone: {adv["marilia_telefone"]}
E-mail: {adv["marilia_email"]}

{adv["eleandro_nome"]}
Telefone: {adv["eleandro_telefone"]}
E-mail: {adv["eleandro_email"]}

Reclamante:

{reclamante.title()}
Telefone: {reclamante_telefone}
E-mail: {reclamante_email}

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


def dados_eletronicos_parceria(
    vara, comarca, processo, reclamante, reclamado,
    id_despacho, reclamante_telefone, reclamante_email,
):
    adv = DADOS_ELETRONICOS_ADVOGADOS
    intro = f"em atenção à decisão de ID {id_despacho}, " if id_despacho.strip() else ""

    return f"""AO JUÍZO DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{reclamante.upper()}**, por seus advogados, nos autos da ação que move contra **{reclamado.upper()}**, vem, respeitosamente, à presença de Vossa Excelência, {intro}informar os dados digitais seus e de seus procuradores, conforme abaixo:

Procuradores:

{adv["marilia_nome"]}
Telefone: {adv["marilia_telefone"]}
E-mail: {adv["marilia_email"]}

{adv["eleandro_nome"]}
Telefone: {adv["eleandro_telefone"]}
E-mail: {adv["eleandro_email"]}

Reclamante:

{reclamante.title()}
Telefone: {reclamante_telefone}
E-mail: {reclamante_email}

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


# ══════════════════════════════════════════════════
# DADOS BANCÁRIOS + ELETRÔNICOS (COMBO)
# ══════════════════════════════════════════════════

def dados_bancarios_eletronicos_noronha(
    vara, comarca, processo, reclamante, reclamado,
    titular, cpf_cnpj, banco, agencia, conta,
    id_despacho, reclamante_telefone, reclamante_email,
):
    adv = DADOS_ELETRONICOS_ADVOGADOS
    intro = f"em atenção à decisão de ID {id_despacho}, " if id_despacho.strip() else ""

    return f"""EXCELENTÍSSIMO(A) SENHOR(A) JUIZ(A) DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{reclamante.upper()}**, por seus advogados signatários, vem, respeitosamente, à Douta e Elevada presença de Vossa Excelência, nos autos da reclamatória trabalhista que move em face de **{reclamado.upper()}**, {intro}informar os dados bancários e eletrônicos seus e de seus procuradores, conforme abaixo:

Dados bancários para fins de pagamento:

Titular: {titular}
CNPJ/CPF: {cpf_cnpj}
Banco: {banco}
Agência: {agencia}
Conta: {conta}

Dados eletrônicos dos procuradores:

Procuradores:

{adv["marilia_nome"]}
Telefone: {adv["marilia_telefone"]}
E-mail: {adv["marilia_email"]}

{adv["eleandro_nome"]}
Telefone: {adv["eleandro_telefone"]}
E-mail: {adv["eleandro_email"]}

Reclamante:

{reclamante.title()}
Telefone: {reclamante_telefone}
E-mail: {reclamante_email}

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


def dados_bancarios_eletronicos_parceria(
    vara, comarca, processo, reclamante, reclamado,
    titular, cpf_cnpj, banco, agencia, conta,
    id_despacho, reclamante_telefone, reclamante_email,
):
    adv = DADOS_ELETRONICOS_ADVOGADOS
    intro = f"em atenção à decisão de ID {id_despacho}, " if id_despacho.strip() else ""

    return f"""AO JUÍZO DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{reclamante.upper()}**, por seus advogados, nos autos da ação que move contra **{reclamado.upper()}**, vem, respeitosamente, à presença de Vossa Excelência, {intro}informar os dados bancários e eletrônicos seus e de seus procuradores, conforme abaixo:

Dados bancários para fins de pagamento:

Titular: {titular}
CNPJ/CPF: {cpf_cnpj}
Banco: {banco}
Agência: {agencia}
Conta Corrente: {conta}

Dados eletrônicos dos procuradores:

Procuradores:

{adv["marilia_nome"]}
Telefone: {adv["marilia_telefone"]}
E-mail: {adv["marilia_email"]}

{adv["eleandro_nome"]}
Telefone: {adv["eleandro_telefone"]}
E-mail: {adv["eleandro_email"]}

Reclamante:

{reclamante.title()}
Telefone: {reclamante_telefone}
E-mail: {reclamante_email}

Nestes termos, pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


# ══════════════════════════════════════════════════
# JUÍZO 100% DIGITAL
# ══════════════════════════════════════════════════

def juizo_100_digital_noronha(
    vara, comarca, processo, reclamante, reclamado, id_despacho, aceita,
):
    texto = (
        "A parte reclamante opta pela tramitação do feito pelo Juízo 100% Digital, "
        "nos termos do art. 3º, §4º, da Resolução nº 378/2021 do CNJ."
        if aceita
        else "A parte reclamante não possui interesse na tramitação do feito pelo Juízo 100% Digital."
    )
    intro = f"em atenção à decisão de ID {id_despacho}, " if id_despacho.strip() else ""

    return f"""EXCELENTÍSSIMO(A) SENHOR(A) JUIZ(A) DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{reclamante.upper()}**, por seus advogados signatários, vem, respeitosamente, à Douta e Elevada presença de Vossa Excelência, nos autos da reclamatória trabalhista que move em face de **{reclamado.upper()}**, {intro}manifestar-se nos seguintes termos:

{texto}

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


def juizo_100_digital_parceria(
    vara, comarca, processo, reclamante, reclamado, id_despacho, aceita,
):
    texto = (
        "A parte reclamante opta pela tramitação do feito pelo Juízo 100% Digital, "
        "nos termos do art. 3º, §4º, da Resolução nº 378/2021 do CNJ."
        if aceita
        else "A parte reclamante não possui interesse na tramitação do feito pelo Juízo 100% Digital."
    )
    intro = f"em atenção à decisão de ID {id_despacho}, " if id_despacho.strip() else ""

    return f"""AO JUÍZO DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{reclamante.upper()}**, por seus advogados, nos autos da ação que move contra **{reclamado.upper()}**, vem, respeitosamente, à presença de Vossa Excelência, {intro}manifestar-se nos seguintes termos:

{texto}

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


# ══════════════════════════════════════════════════
# JUÍZO 100% DIGITAL + DADOS ELETRÔNICOS
# ══════════════════════════════════════════════════

def juizo_100_digital_com_dados_noronha(
    vara, comarca, processo, reclamante, reclamado,
    id_despacho, reclamante_telefone, reclamante_email,
):
    adv = DADOS_ELETRONICOS_ADVOGADOS
    intro = f"em atenção à decisão de ID {id_despacho}, " if id_despacho.strip() else ""

    return f"""EXCELENTÍSSIMO(A) SENHOR(A) JUIZ(A) DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{reclamante.upper()}**, por seus advogados signatários, vem, respeitosamente, à Douta e Elevada presença de Vossa Excelência, nos autos da reclamatória trabalhista que move em face de **{reclamado.upper()}**, {intro}informar que a parte autora opta pelo Juízo 100% Digital, nos termos do art. 3º, §4º, da Resolução nº 378/2021 do CNJ, e apresentar os dados eletrônicos seus e de seus procuradores:

Procuradores:

{adv["marilia_nome"]}
Telefone: {adv["marilia_telefone"]}
E-mail: {adv["marilia_email"]}

{adv["eleandro_nome"]}
Telefone: {adv["eleandro_telefone"]}
E-mail: {adv["eleandro_email"]}

Reclamante:

{reclamante.title()}
Telefone: {reclamante_telefone}
E-mail: {reclamante_email}

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


def juizo_100_digital_com_dados_parceria(
    vara, comarca, processo, reclamante, reclamado,
    id_despacho, reclamante_telefone, reclamante_email,
):
    adv = DADOS_ELETRONICOS_ADVOGADOS
    intro = f"em atenção à decisão de ID {id_despacho}, " if id_despacho.strip() else ""

    return f"""AO JUÍZO DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{reclamante.upper()}**, por seus advogados, nos autos da ação que move contra **{reclamado.upper()}**, vem, respeitosamente, à presença de Vossa Excelência, {intro}informar que a parte autora opta pelo Juízo 100% Digital, nos termos do art. 3º, §4º, da Resolução nº 378/2021 do CNJ, e apresentar os dados eletrônicos seus e de seus procuradores:

Procuradores:

{adv["marilia_nome"]}
Telefone: {adv["marilia_telefone"]}
E-mail: {adv["marilia_email"]}

{adv["eleandro_nome"]}
Telefone: {adv["eleandro_telefone"]}
E-mail: {adv["eleandro_email"]}

Reclamante:

{reclamante.title()}
Telefone: {reclamante_telefone}
E-mail: {reclamante_email}

Nestes termos, pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


# ══════════════════════════════════════════════════
# DESINTERESSE EM CONCILIAÇÃO
# ══════════════════════════════════════════════════

def desinteresse_conciliacao_noronha(
    vara, comarca, processo, reclamante, reclamado, id_despacho,
):
    return f"""EXCELENTÍSSIMO(A) SENHOR(A) JUIZ(A) DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{reclamante.upper()}**, por seus advogados signatários, vem, respeitosamente, à Douta e Elevada presença de Vossa Excelência, nos autos da reclamatória trabalhista que move em face de **{reclamado.upper()}**, expor e requerer o que adiante segue:

Tendo em vista a certidão de ID {id_despacho}, a parte reclamante informa que não possui interesse na participação em audiência de conciliação.

Diante do exposto, requer o regular prosseguimento do feito.

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


def desinteresse_conciliacao_parceria(
    vara, comarca, processo, reclamante, reclamado, id_despacho,
):
    return f"""AO JUÍZO DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{reclamante.upper()}**, por seus advogados, nos autos da ação que move contra **{reclamado.upper()}**, vem, respeitosamente, à presença de Vossa Excelência, manifestar que, tendo em vista a certidão de ID {id_despacho}, não possui interesse na participação em audiência de conciliação.

Diante do exposto, requer o regular prosseguimento do feito.

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


# ══════════════════════════════════════════════════
# JUNTADA DE DOCUMENTOS
# ══════════════════════════════════════════════════

def juntada_documentos_noronha(
    vara, comarca, processo, reclamante, reclamado, id_despacho, descricao,
):
    intro_id = f"em atenção à decisão de ID {id_despacho}, " if id_despacho.strip() else ""
    corpo = f"\n{descricao}\n" if descricao.strip() else ""

    return f"""EXCELENTÍSSIMO(A) SENHOR(A) JUIZ(A) DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{reclamante.upper()}**, por seus advogados signatários, vem, respeitosamente, à Douta e Elevada presença de Vossa Excelência, nos autos da reclamatória trabalhista que move em face de **{reclamado.upper()}**, {intro_id}juntar aos autos os documentos ora anexados.
{corpo}
Requer seja juntado o presente documento aos autos para os fins de direito.

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


def juntada_documentos_parceria(
    vara, comarca, processo, reclamante, reclamado, id_despacho, descricao,
):
    intro_id = f"em atenção à decisão de ID {id_despacho}, " if id_despacho.strip() else ""
    corpo = f"\n{descricao}\n" if descricao.strip() else ""

    return f"""AO JUÍZO DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{reclamante.upper()}**, por seus advogados, nos autos da ação que move contra **{reclamado.upper()}**, vem, respeitosamente, à presença de Vossa Excelência, {intro_id}juntar aos autos os documentos ora anexados.
{corpo}
Requer seja juntado o presente documento aos autos para os fins de direito.

Nestes termos, pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


# ══════════════════════════════════════════════════
# JUNTADA DE CÁLCULOS
# ══════════════════════════════════════════════════

def juntada_calculos_noronha(
    vara, comarca, processo, reclamante, reclamado, id_despacho, descricao,
):
    intro_id = f"em atenção à intimação de ID {id_despacho}, " if id_despacho.strip() else ""
    obs = f"\n{descricao}\n" if descricao.strip() else ""

    return f"""EXCELENTÍSSIMO(A) SENHOR(A) JUIZ(A) DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{reclamante.upper()}**, por seus advogados signatários, vem, respeitosamente, à Douta e Elevada presença de Vossa Excelência, nos autos da reclamatória trabalhista que move em face de **{reclamado.upper()}**, {intro_id}juntar planilha de cálculos de liquidação de sentença, conforme demonstrativo em anexo.
{obs}
Requer seja homologado o presente cálculo para os fins de execução.

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


def juntada_calculos_parceria(
    vara, comarca, processo, reclamante, reclamado, id_despacho, descricao,
):
    intro_id = f"em atenção à intimação de ID {id_despacho}, " if id_despacho.strip() else ""
    obs = f"\n{descricao}\n" if descricao.strip() else ""

    return f"""AO JUÍZO DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{reclamante.upper()}**, por seus advogados, nos autos da ação que move contra **{reclamado.upper()}**, vem, respeitosamente, à presença de Vossa Excelência, {intro_id}juntar planilha de cálculos de liquidação de sentença, conforme demonstrativo em anexo.
{obs}
Requer seja homologado o presente cálculo para os fins de execução.

Nestes termos, pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


# ══════════════════════════════════════════════════
# CUMPRIMENTO DE INTIMAÇÃO
# ══════════════════════════════════════════════════

def cumprimento_intimacao_noronha(
    vara, comarca, processo, reclamante, reclamado, id_despacho, descricao,
):
    return f"""EXCELENTÍSSIMO(A) SENHOR(A) JUIZ(A) DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{reclamante.upper()}**, por seus advogados signatários, vem, respeitosamente, à Douta e Elevada presença de Vossa Excelência, nos autos da reclamatória trabalhista que move em face de **{reclamado.upper()}**, em cumprimento à intimação de ID {id_despacho}, informar:

{descricao}

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


def cumprimento_intimacao_parceria(
    vara, comarca, processo, reclamante, reclamado, id_despacho, descricao,
):
    return f"""AO JUÍZO DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{reclamante.upper()}**, por seus advogados, nos autos da ação que move contra **{reclamado.upper()}**, vem, respeitosamente, à presença de Vossa Excelência, em cumprimento à intimação de ID {id_despacho}, informar:

{descricao}

Nestes termos, pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


# ══════════════════════════════════════════════════
# AUDIÊNCIA TELEPRESENCIAL
# ══════════════════════════════════════════════════

def audiencia_telepresencial_noronha(
    vara, comarca, processo, reclamante, reclamado, id_despacho, motivo,
):
    intro_id = f"em atenção à intimação de ID {id_despacho}, " if id_despacho.strip() else ""
    motivo_texto = motivo.strip() if motivo.strip() else "razões de ordem pessoal e logística"

    return f"""EXCELENTÍSSIMO(A) SENHOR(A) JUIZ(A) DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{reclamante.upper()}**, por seus advogados signatários, vem, respeitosamente, à Douta e Elevada presença de Vossa Excelência, nos autos da reclamatória trabalhista que move em face de **{reclamado.upper()}**, {intro_id}requerer a realização da audiência por videoconferência (telepresencial), tendo em vista que {motivo_texto}.

Requer, portanto, seja deferida a realização da audiência por meio de plataforma digital, nos termos do art. 13 da IN nº 41/2018 do TST.

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


def audiencia_telepresencial_parceria(
    vara, comarca, processo, reclamante, reclamado, id_despacho, motivo,
):
    intro_id = f"em atenção à intimação de ID {id_despacho}, " if id_despacho.strip() else ""
    motivo_texto = motivo.strip() if motivo.strip() else "razões de ordem pessoal e logística"

    return f"""AO JUÍZO DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{reclamante.upper()}**, por seus advogados, nos autos da ação que move contra **{reclamado.upper()}**, vem, respeitosamente, à presença de Vossa Excelência, {intro_id}requerer a realização da audiência por videoconferência (telepresencial), tendo em vista que {motivo_texto}.

Requer, portanto, seja deferida a realização da audiência por meio de plataforma digital, nos termos do art. 13 da IN nº 41/2018 do TST.

Nestes termos, pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


# ══════════════════════════════════════════════════
# MANIFESTAÇÃO SIMPLES
# ══════════════════════════════════════════════════

def manifestacao_simples_noronha(
    vara, comarca, processo, reclamante, reclamado, id_despacho, texto,
):
    intro_id = f"em atenção à decisão de ID {id_despacho}, " if id_despacho.strip() else ""

    return f"""EXCELENTÍSSIMO(A) SENHOR(A) JUIZ(A) DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{reclamante.upper()}**, por seus advogados signatários, vem, respeitosamente, à Douta e Elevada presença de Vossa Excelência, nos autos da reclamatória trabalhista que move em face de **{reclamado.upper()}**, {intro_id}manifestar-se nos seguintes termos:

{texto}

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


def manifestacao_simples_parceria(
    vara, comarca, processo, reclamante, reclamado, id_despacho, texto,
):
    intro_id = f"em atenção à decisão de ID {id_despacho}, " if id_despacho.strip() else ""

    return f"""AO JUÍZO DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{reclamante.upper()}**, por seus advogados, nos autos da ação que move contra **{reclamado.upper()}**, vem, respeitosamente, à presença de Vossa Excelência, {intro_id}manifestar-se nos seguintes termos:

{texto}

Nestes termos, pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


# ══════════════════════════════════════════════════
# PEDIDO GENÉRICO
# ══════════════════════════════════════════════════

def pedido_generico_noronha(vara, comarca, processo, reclamante, reclamado, texto):
    return f"""EXCELENTÍSSIMO(A) SENHOR(A) JUIZ(A) DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{reclamante.upper()}**, por seus advogados signatários, vem, respeitosamente, à Douta e Elevada presença de Vossa Excelência, nos autos da reclamatória trabalhista que move em face de **{reclamado.upper()}**, expor e requerer o que adiante segue:

{texto}

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


def pedido_generico_parceria(vara, comarca, processo, reclamante, reclamado, texto):
    return f"""AO JUÍZO DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{reclamante.upper()}**, por seus advogados, nos autos da ação que move contra **{reclamado.upper()}**, vem, respeitosamente, à presença de Vossa Excelência, requerer o que segue:

{texto}

Nestes termos, pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


# ══════════════════════════════════════════════════
# INTERESSE EM CONCILIAÇÃO / CEJUSC-2G
# ══════════════════════════════════════════════════

import re as _re


def _regiao_trt(processo: str) -> str:
    m = _re.search(r'\d{7}-\d{2}[.\-]\d{4}[.\-]\d[.\-](\d{2})[.\-]\d{4}', processo)
    return str(int(m.group(1))) if m else "4"


def interesse_conciliacao_noronha(processo, reclamante, reclamado):
    regiao = _regiao_trt(processo)
    return f"""AO JUÍZO DO TRIBUNAL REGIONAL DO TRABALHO DA {regiao}ª REGIÃO

Processo nº {processo}

**{reclamante.upper()}**, já qualificado nos autos da reclamatória trabalhista promovida em face do **{reclamado.upper()}**, também já qualificado, vem, respeitosamente, à presença de Vossa Excelência, por meio de seus procuradores, dizer e requerer o que segue:

Em atenção à intimação para que as partes se manifestem sobre o interesse em conciliar mediante designação de audiência conciliatória ou apresentação de proposta de conciliação, o reclamante vem informar que **possui interesse na realização de audiência de conciliação**, requerendo, assim, a **remessa dos autos ao CEJUSC-2G** para as providências cabíveis.

Nestes termos, pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


def interesse_conciliacao_parceria(processo, reclamante, reclamado):
    regiao = _regiao_trt(processo)
    return f"""AO JUÍZO DO TRIBUNAL REGIONAL DO TRABALHO DA {regiao}ª REGIÃO

Processo nº {processo}

**{reclamante.upper()}**, já qualificado nos autos da reclamatória trabalhista promovida em face do **{reclamado.upper()}**, também já qualificado, vem, respeitosamente, à presença de Vossa Excelência, por meio de seus procuradores, dizer e requerer o que segue:

Em atenção à intimação para que as partes se manifestem sobre o interesse em conciliar mediante designação de audiência conciliatória ou apresentação de proposta de conciliação, o reclamante vem informar que **possui interesse na realização de audiência de conciliação**, requerendo, assim, a **remessa dos autos ao CEJUSC-2G** para as providências cabíveis.

Nestes termos, pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


# ══════════════════════════════════════════════════
# INTERESSE EM AUDIÊNCIA DE CONCILIAÇÃO TELEPRESENCIAL
# ══════════════════════════════════════════════════

def interesse_audiencia_conciliacao_noronha(
    vara, comarca, processo, reclamante, reclamado, id_despacho,
):
    intro_id = f"em atenção à intimação de ID {id_despacho}, " if id_despacho.strip() else ""

    return f"""EXCELENTÍSSIMO(A) SENHOR(A) JUIZ(A) DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{reclamante.upper()}**, por seus advogados signatários, vem, respeitosamente, à Douta e Elevada presença de Vossa Excelência, nos autos da reclamatória trabalhista que move em face de **{reclamado.upper()}**, {intro_id}manifestar-se nos seguintes termos:

O reclamante informa que POSSUI INTERESSE na realização de audiência exclusivamente para tratativas de conciliação, de forma telepresencial, por meio da plataforma de videoconferência Zoom, nos termos da intimação.

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


def interesse_audiencia_conciliacao_parceria(
    vara, comarca, processo, reclamante, reclamado, id_despacho,
):
    intro_id = f"em atenção à intimação de ID {id_despacho}, " if id_despacho.strip() else ""

    return f"""AO JUÍZO DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{reclamante.upper()}**, já qualificado nos autos da reclamatória trabalhista promovida em face de **{reclamado.upper()}**, também já qualificado, vem, respeitosamente, à presença de Vossa Excelência, por meio de seus procuradores, {intro_id}dizer e requerer o que segue:

O reclamante informa que POSSUI INTERESSE na realização de audiência exclusivamente para tratativas de conciliação, de forma telepresencial, por meio da plataforma de videoconferência Zoom, nos termos da intimação.

Nestes termos, pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


# ══════════════════════════════════════════════════
# IMPUGNAÇÃO AOS CÁLCULOS
# ══════════════════════════════════════════════════

def impugnacao_calculos_noronha(
    vara, comarca, processo, reclamante, reclamado, id_despacho,
):
    ref_id = f" de ID {id_despacho}" if id_despacho.strip() else ""

    return f"""EXCELENTÍSSIMO(A) SENHOR(A) JUIZ(A) DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{reclamante.upper()}**, por seus advogados signatários, vem, respeitosamente, à Douta e Elevada presença de Vossa Excelência, nos autos da reclamatória trabalhista que move em face de **{reclamado.upper()}**, expor e requerer o que adiante segue:

Em atenção à intimação{ref_id}, vem apresentar IMPUGNAÇÃO AOS CÁLCULOS DE LIQUIDAÇÃO apresentados pela reclamada, nos termos do art. 879, §2º, da CLT, conforme razões e demonstrativo em anexo.

Requer seja apreciada a presente impugnação e, acolhidas as razões expostas, seja determinada a retificação dos cálculos para fins de execução.

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


def impugnacao_calculos_parceria(
    vara, comarca, processo, reclamante, reclamado, id_despacho,
):
    ref_id = f" de ID {id_despacho}" if id_despacho.strip() else ""

    return f"""AO JUÍZO DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{reclamante.upper()}**, já qualificado nos autos da reclamatória trabalhista promovida em face de **{reclamado.upper()}**, também já qualificado, vem, respeitosamente, à presença de Vossa Excelência, por meio de seus procuradores, dizer e requerer o que segue:

Em atenção à intimação{ref_id}, vem apresentar IMPUGNAÇÃO AOS CÁLCULOS DE LIQUIDAÇÃO apresentados pela reclamada, nos termos do art. 879, §2º, da CLT, conforme razões e demonstrativo em anexo.

Requer seja apreciada a presente impugnação e, acolhidas as razões expostas, seja determinada a retificação dos cálculos para fins de execução.

Nestes termos, pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


# ══════════════════════════════════════════════════
# CONCORDÂNCIA COM OS CÁLCULOS  ← NOVO
# ══════════════════════════════════════════════════

def concordancia_calculos_noronha(
    vara, comarca, processo, reclamante, reclamado, id_despacho,
):
    ref_id = f" de ID {id_despacho}" if id_despacho.strip() else ""

    return f"""EXCELENTÍSSIMO(A) SENHOR(A) JUIZ(A) DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{reclamante.upper()}**, por seus advogados signatários, vem, respeitosamente, à Douta e Elevada presença de Vossa Excelência, nos autos da reclamatória trabalhista que move em face de **{reclamado.upper()}**, expor e requerer o que adiante segue:

Em atenção à intimação{ref_id}, a parte reclamante informa que CONCORDA com os cálculos de liquidação apresentados pela reclamada, requerendo a homologação dos valores apurados e o regular prosseguimento do feito executivo.

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


def concordancia_calculos_parceria(
    vara, comarca, processo, reclamante, reclamado, id_despacho,
):
    ref_id = f" de ID {id_despacho}" if id_despacho.strip() else ""

    return f"""AO JUÍZO DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{reclamante.upper()}**, já qualificado nos autos da reclamatória trabalhista promovida em face de **{reclamado.upper()}**, também já qualificado, vem, respeitosamente, à presença de Vossa Excelência, por meio de seus procuradores, dizer e requerer o que segue:

Em atenção à intimação{ref_id}, a parte reclamante informa que CONCORDA com os cálculos de liquidação apresentados pela reclamada, requerendo a homologação dos valores apurados e o regular prosseguimento do feito executivo.

Nestes termos, pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""