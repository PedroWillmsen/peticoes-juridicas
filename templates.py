from datetime import date
import re as _re
from constants import DADOS_ELETRONICOS_ADVOGADOS


def _ano() -> int:
    return date.today().year


def format_juizo(vara: str, comarca: str) -> str:
    return f"{vara.upper()} DE {comarca.upper()}/RS."


def _nome(s: str) -> str:
    """Uppercase + corrige SA → S.A."""
    s = s.upper()
    s = _re.sub(r'\bSA\b', 'S.A.', s)
    return s


# ══════════════════════════════════════════════════
# DADOS BANCÁRIOS
# ══════════════════════════════════════════════════

def dados_bancarios_noronha(
    vara, comarca, processo, reclamante, reclamado,
    titular, cpf_cnpj, banco, agencia, conta,
):
    return f"""EXCELENTÍSSIMO(A) SENHOR(A) JUIZ(A) DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{_nome(reclamante)}**, por seus advogados signatários, vem, respeitosamente, à Douta e Elevada presença de Vossa Excelência, nos autos da reclamação trabalhista que move em face de **{_nome(reclamado)}**, expor e requerer o que adiante segue:

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

**{_nome(reclamante)}**, já qualificado nos autos da reclamação trabalhista promovida em face de **{_nome(reclamado)}**, também já qualificado, vem, respeitosamente, à presença de Vossa Excelência, por meio de seus procuradores, dizer e requerer o que segue:

Tendo em vista a necessidade de informação de dados bancários para fins de liberação de valores, o exequente informa os dados bancários de seu procurador, com poderes para tanto, para transferência eletrônica:

Titular: {titular}
CNPJ/CPF: {cpf_cnpj}
Banco: {banco}
Agência: {agencia}
Conta Corrente: {conta}

Termos em que pede deferimento.

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
    if id_despacho.strip():
        id_txt = f"Em atenção à decisão de ID {id_despacho}, informa"
    else:
        id_txt = "Vem informar"

    return f"""EXCELENTÍSSIMO(A) SENHOR(A) JUIZ(A) DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{_nome(reclamante)}**, por seus advogados signatários, vem, respeitosamente, à Douta e Elevada presença de Vossa Excelência, nos autos da reclamação trabalhista que move em face de **{_nome(reclamado)}**, expor e requerer o que adiante segue:

{id_txt} os dados eletrônicos seus e de seus procuradores, conforme abaixo:

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
    if id_despacho.strip():
        id_txt = f"Em atenção à decisão de ID {id_despacho}, informa"
    else:
        id_txt = "Vem informar"

    return f"""AO JUÍZO DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{_nome(reclamante)}**, já qualificado, por seus advogados, nos autos da reclamação que move contra **{_nome(reclamado)}**, vem, respeitosamente, à presença de Vossa Excelência, expor e requerer o que segue:

{id_txt} os dados digitais seus e de seus procuradores, conforme abaixo:

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
    if id_despacho.strip():
        id_txt = f"Em atenção à decisão de ID {id_despacho}, informa"
    else:
        id_txt = "Vem informar"

    return f"""EXCELENTÍSSIMO(A) SENHOR(A) JUIZ(A) DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{_nome(reclamante)}**, por seus advogados signatários, vem, respeitosamente, à Douta e Elevada presença de Vossa Excelência, nos autos da reclamação trabalhista que move em face de **{_nome(reclamado)}**, expor e requerer o que adiante segue:

{id_txt} os dados bancários e eletrônicos seus e de seus procuradores, conforme abaixo:

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
    if id_despacho.strip():
        id_txt = f"Em atenção à decisão de ID {id_despacho}, informa"
    else:
        id_txt = "Vem informar"

    return f"""AO JUÍZO DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{_nome(reclamante)}**, já qualificado, por seus advogados, nos autos da reclamação que move contra **{_nome(reclamado)}**, vem, respeitosamente, à presença de Vossa Excelência, expor e requerer o que segue:

{id_txt} os dados bancários e eletrônicos seus e de seus procuradores, conforme abaixo:

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

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


# ══════════════════════════════════════════════════
# JUÍZO 100% DIGITAL
# ══════════════════════════════════════════════════

def juizo_100_digital_noronha(
    vara, comarca, processo, reclamante, reclamado, id_despacho, aceita,
):
    opcao = (
        "a parte reclamante opta pela tramitação do feito pelo Juízo 100% Digital, "
        "nos termos do art. 3º, §4º, da Resolução nº 378/2021 do CNJ."
        if aceita
        else "a parte reclamante não possui interesse na tramitação do feito pelo Juízo 100% Digital."
    )
    if id_despacho.strip():
        texto = f"Em atenção à decisão de ID {id_despacho}, {opcao}"
    else:
        texto = opcao.capitalize()

    return f"""EXCELENTÍSSIMO(A) SENHOR(A) JUIZ(A) DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{_nome(reclamante)}**, por seus advogados signatários, vem, respeitosamente, à Douta e Elevada presença de Vossa Excelência, nos autos da reclamação trabalhista que move em face de **{_nome(reclamado)}**, expor e requerer o que adiante segue:

{texto}

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


def juizo_100_digital_parceria(
    vara, comarca, processo, reclamante, reclamado, id_despacho, aceita,
):
    opcao = (
        "a parte reclamante opta pela tramitação do feito pelo Juízo 100% Digital, "
        "nos termos do art. 3º, §4º, da Resolução nº 378/2021 do CNJ."
        if aceita
        else "a parte reclamante não possui interesse na tramitação do feito pelo Juízo 100% Digital."
    )
    if id_despacho.strip():
        texto = f"Em atenção à decisão de ID {id_despacho}, {opcao}"
    else:
        texto = opcao.capitalize()

    return f"""AO JUÍZO DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{_nome(reclamante)}**, já qualificado, por seus advogados, nos autos da reclamação que move contra **{_nome(reclamado)}**, vem, respeitosamente, à presença de Vossa Excelência, expor e requerer o que segue:

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
    if id_despacho.strip():
        id_txt = f"Em atenção à decisão de ID {id_despacho}, informa"
    else:
        id_txt = "Informa"

    return f"""EXCELENTÍSSIMO(A) SENHOR(A) JUIZ(A) DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{_nome(reclamante)}**, por seus advogados signatários, vem, respeitosamente, à Douta e Elevada presença de Vossa Excelência, nos autos da reclamação trabalhista que move em face de **{_nome(reclamado)}**, expor e requerer o que adiante segue:

{id_txt} que a parte autora opta pelo Juízo 100% Digital, nos termos do art. 3º, §4º, da Resolução nº 378/2021 do CNJ, e apresentar os dados eletrônicos seus e de seus procuradores:

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
    if id_despacho.strip():
        id_txt = f"Em atenção à decisão de ID {id_despacho}, informa"
    else:
        id_txt = "Informa"

    return f"""AO JUÍZO DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{_nome(reclamante)}**, já qualificado, por seus advogados, nos autos da reclamação que move contra **{_nome(reclamado)}**, vem, respeitosamente, à presença de Vossa Excelência, expor e requerer o que segue:

{id_txt} que a parte autora opta pelo Juízo 100% Digital, nos termos do art. 3º, §4º, da Resolução nº 378/2021 do CNJ, e apresentar os dados eletrônicos seus e de seus procuradores:

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
# DESINTERESSE EM CONCILIAÇÃO
# ══════════════════════════════════════════════════

def desinteresse_conciliacao_noronha(
    vara, comarca, processo, reclamante, reclamado, id_despacho,
):
    if id_despacho.strip():
        corpo = f"Em atenção à intimação de ID {id_despacho}, a parte reclamante informa que não possui interesse na participação em audiência de conciliação."
    else:
        corpo = "A parte reclamante informa que não possui interesse na participação em audiência de conciliação."

    return f"""EXCELENTÍSSIMO(A) SENHOR(A) JUIZ(A) DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{_nome(reclamante)}**, por seus advogados signatários, vem, respeitosamente, à Douta e Elevada presença de Vossa Excelência, nos autos da reclamação trabalhista que move em face de **{_nome(reclamado)}**, expor e requerer o que adiante segue:

{corpo}

Diante do exposto, requer o regular prosseguimento do feito.

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


def desinteresse_conciliacao_parceria(
    vara, comarca, processo, reclamante, reclamado, id_despacho,
):
    if id_despacho.strip():
        corpo = f"Em atenção à intimação de ID {id_despacho}, a parte reclamante informa que não possui interesse na participação em audiência de conciliação."
    else:
        corpo = "A parte reclamante informa que não possui interesse na participação em audiência de conciliação."

    return f"""AO JUÍZO DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{_nome(reclamante)}**, já qualificado, por seus advogados, nos autos da ação que move contra **{_nome(reclamado)}**, vem, respeitosamente, à presença de Vossa Excelência, expor e requerer o que segue:

{corpo}

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
    if id_despacho.strip():
        acao = f"Em atenção à decisão de ID {id_despacho}, requer"
    else:
        acao = "Requer"
    corpo = f"\n{descricao}\n" if descricao.strip() else ""

    return f"""EXCELENTÍSSIMO(A) SENHOR(A) JUIZ(A) DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{_nome(reclamante)}**, por seus advogados signatários, vem, respeitosamente, à Douta e Elevada presença de Vossa Excelência, nos autos da reclamação trabalhista que move em face de **{_nome(reclamado)}**, expor e requerer o que adiante segue:

{acao} a juntada aos autos dos documentos ora anexados.{corpo}

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


def juntada_documentos_parceria(
    vara, comarca, processo, reclamante, reclamado, id_despacho, descricao,
):
    if id_despacho.strip():
        acao = f"Em atenção à decisão de ID {id_despacho}, requer"
    else:
        acao = "Requer"
    corpo = f"\n{descricao}\n" if descricao.strip() else ""

    return f"""AO JUÍZO DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{_nome(reclamante)}**, já qualificado, por seus advogados, nos autos da ação que move contra **{_nome(reclamado)}**, vem, respeitosamente, à presença de Vossa Excelência, expor e requerer o que segue:

{acao} a juntada aos autos dos documentos ora anexados.{corpo}

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


# ══════════════════════════════════════════════════
# JUNTADA DE CÁLCULOS
# ══════════════════════════════════════════════════

def juntada_calculos_noronha(
    vara, comarca, processo, reclamante, reclamado, id_despacho, descricao,
):
    if id_despacho.strip():
        acao = f"Em atenção à intimação de ID {id_despacho}, requer"
    else:
        acao = "Requer"
    obs = f"\n{descricao}\n" if descricao.strip() else ""

    return f"""EXCELENTÍSSIMO(A) SENHOR(A) JUIZ(A) DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{_nome(reclamante)}**, por seus advogados signatários, vem, respeitosamente, à Douta e Elevada presença de Vossa Excelência, nos autos da reclamação trabalhista que move em face de **{_nome(reclamado)}**, expor e requerer o que adiante segue:

{acao} a juntada da planilha de cálculos de liquidação de sentença, conforme demonstrativo em anexo.{obs}

Requer seja homologado o presente cálculo para os fins de execução.

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


def juntada_calculos_parceria(
    vara, comarca, processo, reclamante, reclamado, id_despacho, descricao,
):
    if id_despacho.strip():
        acao = f"Em atenção à intimação de ID {id_despacho}, requer"
    else:
        acao = "Requer"
    obs = f"\n{descricao}\n" if descricao.strip() else ""

    return f"""AO JUÍZO DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{_nome(reclamante)}**, já qualificado, por seus advogados, nos autos da ação que move contra **{_nome(reclamado)}**, vem, respeitosamente, à presença de Vossa Excelência, expor e requerer o que segue:

{acao} a juntada da planilha de cálculos de liquidação de sentença, conforme demonstrativo em anexo.{obs}

Requer seja homologado o presente cálculo para os fins de execução.

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


# ══════════════════════════════════════════════════
# CUMPRIMENTO DE INTIMAÇÃO
# ══════════════════════════════════════════════════

def cumprimento_intimacao_noronha(
    vara, comarca, processo, reclamante, reclamado, id_despacho, descricao,
):
    if id_despacho.strip():
        intro_corpo = f"Em cumprimento à intimação de ID {id_despacho}, informa:"
    else:
        intro_corpo = "Em cumprimento à intimação, informa:"

    return f"""EXCELENTÍSSIMO(A) SENHOR(A) JUIZ(A) DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{_nome(reclamante)}**, por seus advogados signatários, vem, respeitosamente, à Douta e Elevada presença de Vossa Excelência, nos autos da reclamação trabalhista que move em face de **{_nome(reclamado)}**, expor e requerer o que adiante segue:

{intro_corpo}

{descricao}

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


def cumprimento_intimacao_parceria(
    vara, comarca, processo, reclamante, reclamado, id_despacho, descricao,
):
    if id_despacho.strip():
        intro_corpo = f"Em cumprimento à intimação de ID {id_despacho}, informa:"
    else:
        intro_corpo = "Em cumprimento à intimação, informa:"

    return f"""AO JUÍZO DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{_nome(reclamante)}**, já qualificado, por seus advogados, nos autos da ação que move contra **{_nome(reclamado)}**, vem, respeitosamente, à presença de Vossa Excelência, expor e requerer o que segue:

{intro_corpo}

{descricao}

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


# ══════════════════════════════════════════════════
# AUDIÊNCIA TELEPRESENCIAL
# ══════════════════════════════════════════════════

def audiencia_telepresencial_noronha(
    vara, comarca, processo, reclamante, reclamado, id_despacho, motivo,
):
    motivo_texto = motivo.strip() if motivo.strip() else "razões de ordem pessoal e logística"
    if id_despacho.strip():
        acao = f"Em atenção à intimação de ID {id_despacho}, requer"
    else:
        acao = "Requer"

    return f"""EXCELENTÍSSIMO(A) SENHOR(A) JUIZ(A) DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{_nome(reclamante)}**, por seus advogados signatários, vem, respeitosamente, à Douta e Elevada presença de Vossa Excelência, nos autos da reclamação trabalhista que move em face de **{_nome(reclamado)}**, expor e requerer o que adiante segue:

{acao} a realização da audiência por videoconferência (telepresencial), tendo em vista que {motivo_texto}.

Requer, portanto, seja deferida a realização da audiência por meio de plataforma digital, nos termos do art. 13 da IN nº 41/2018 do TST.

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


def audiencia_telepresencial_parceria(
    vara, comarca, processo, reclamante, reclamado, id_despacho, motivo,
):
    motivo_texto = motivo.strip() if motivo.strip() else "razões de ordem pessoal e logística"
    if id_despacho.strip():
        acao = f"Em atenção à intimação de ID {id_despacho}, requer"
    else:
        acao = "Requer"

    return f"""AO JUÍZO DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{_nome(reclamante)}**, já qualificado, por seus advogados, nos autos da ação que move contra **{_nome(reclamado)}**, vem, respeitosamente, à presença de Vossa Excelência, expor e requerer o que segue:

{acao} a realização da audiência por videoconferência (telepresencial), tendo em vista que {motivo_texto}.

Requer, portanto, seja deferida a realização da audiência por meio de plataforma digital, nos termos do art. 13 da IN nº 41/2018 do TST.

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


# ══════════════════════════════════════════════════
# MANIFESTAÇÃO SIMPLES
# ══════════════════════════════════════════════════

def manifestacao_simples_noronha(
    vara, comarca, processo, reclamante, reclamado, id_despacho, texto,
):
    if id_despacho.strip():
        intro_corpo = f"Em atenção à decisão de ID {id_despacho}, manifesta-se nos seguintes termos:"
    else:
        intro_corpo = "Vem manifestar-se nos seguintes termos:"

    return f"""EXCELENTÍSSIMO(A) SENHOR(A) JUIZ(A) DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{_nome(reclamante)}**, por seus advogados signatários, vem, respeitosamente, à Douta e Elevada presença de Vossa Excelência, nos autos da reclamação trabalhista que move em face de **{_nome(reclamado)}**, expor e requerer o que adiante segue:

{intro_corpo}

{texto}

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


def manifestacao_simples_parceria(
    vara, comarca, processo, reclamante, reclamado, id_despacho, texto,
):
    if id_despacho.strip():
        intro_corpo = f"Em atenção à decisão de ID {id_despacho}, manifesta-se nos seguintes termos:"
    else:
        intro_corpo = "Vem manifestar-se nos seguintes termos:"

    return f"""AO JUÍZO DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{_nome(reclamante)}**, já qualificado, por seus advogados, nos autos da ação que move contra **{_nome(reclamado)}**, vem, respeitosamente, à presença de Vossa Excelência, expor e requerer o que segue:

{intro_corpo}

{texto}

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


# ══════════════════════════════════════════════════
# PEDIDO GENÉRICO
# ══════════════════════════════════════════════════

def pedido_generico_noronha(vara, comarca, processo, reclamante, reclamado, texto):
    return f"""EXCELENTÍSSIMO(A) SENHOR(A) JUIZ(A) DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{_nome(reclamante)}**, por seus advogados signatários, vem, respeitosamente, à Douta e Elevada presença de Vossa Excelência, nos autos da reclamação trabalhista que move em face de **{_nome(reclamado)}**, expor e requerer o que adiante segue:

{texto}

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


def pedido_generico_parceria(vara, comarca, processo, reclamante, reclamado, texto):
    return f"""AO JUÍZO DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{_nome(reclamante)}**, já qualificado, por seus advogados, nos autos da ação que move contra **{_nome(reclamado)}**, vem, respeitosamente, à presença de Vossa Excelência, expor e requerer o que segue:

{texto}

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


# ══════════════════════════════════════════════════
# INTERESSE EM CONCILIAÇÃO / CEJUSC-2G
# ══════════════════════════════════════════════════

def _regiao_trt(processo: str) -> str:
    m = _re.search(r'\d{7}-\d{2}[.\-]\d{4}[.\-]\d[.\-](\d{2})[.\-]\d{4}', processo)
    return str(int(m.group(1))) if m else "4"


def interesse_conciliacao_noronha(processo, reclamante, reclamado):
    regiao = _regiao_trt(processo)
    return f"""AO JUÍZO DO TRIBUNAL REGIONAL DO TRABALHO DA {regiao}ª REGIÃO

Processo nº {processo}

**{_nome(reclamante)}**, já qualificado nos autos da reclamatória trabalhista promovida em face do **{_nome(reclamado)}**, também já qualificado, vem, respeitosamente, à presença de Vossa Excelência, por meio de seus procuradores, dizer e requerer o que segue:

Em atenção à intimação para que as partes se manifestem sobre o interesse em conciliar mediante designação de audiência conciliatória ou apresentação de proposta de conciliação, o reclamante vem informar que **possui interesse na realização de audiência de conciliação**, requerendo, assim, a **remessa dos autos ao CEJUSC-2G** para as providências cabíveis.

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


def interesse_conciliacao_parceria(processo, reclamante, reclamado):
    regiao = _regiao_trt(processo)
    return f"""AO JUÍZO DO TRIBUNAL REGIONAL DO TRABALHO DA {regiao}ª REGIÃO

Processo nº {processo}

**{_nome(reclamante)}**, já qualificado nos autos da reclamatória trabalhista promovida em face do **{_nome(reclamado)}**, também já qualificado, vem, respeitosamente, à presença de Vossa Excelência, por meio de seus procuradores, dizer e requerer o que segue:

Em atenção à intimação para que as partes se manifestem sobre o interesse em conciliar mediante designação de audiência conciliatória ou apresentação de proposta de conciliação, o reclamante vem informar que **possui interesse na realização de audiência de conciliação**, requerendo, assim, a **remessa dos autos ao CEJUSC-2G** para as providências cabíveis.

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


# ══════════════════════════════════════════════════
# INTERESSE EM AUDIÊNCIA DE CONCILIAÇÃO TELEPRESENCIAL
# ══════════════════════════════════════════════════

def interesse_audiencia_conciliacao_noronha(
    vara, comarca, processo, reclamante, reclamado, id_despacho,
):
    if id_despacho.strip():
        intro_corpo = f"Em atenção à intimação de ID {id_despacho}, o reclamante"
    else:
        intro_corpo = "O reclamante"

    return f"""EXCELENTÍSSIMO(A) SENHOR(A) JUIZ(A) DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{_nome(reclamante)}**, por seus advogados signatários, vem, respeitosamente, à Douta e Elevada presença de Vossa Excelência, nos autos da reclamação trabalhista que move em face de **{_nome(reclamado)}**, expor e requerer o que adiante segue:

{intro_corpo} informa que POSSUI INTERESSE na realização de audiência exclusivamente para tratativas de conciliação, de forma telepresencial, por meio da plataforma de videoconferência Zoom, nos termos da intimação.

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


def interesse_audiencia_conciliacao_parceria(
    vara, comarca, processo, reclamante, reclamado, id_despacho,
):
    if id_despacho.strip():
        intro_corpo = f"Em atenção à intimação de ID {id_despacho}, o reclamante"
    else:
        intro_corpo = "O reclamante"

    return f"""AO JUÍZO DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{_nome(reclamante)}**, já qualificado nos autos da reclamatória trabalhista promovida em face de **{_nome(reclamado)}**, também já qualificado, vem, respeitosamente, à presença de Vossa Excelência, por meio de seus procuradores, dizer e requerer o que segue:

{intro_corpo} informa que POSSUI INTERESSE na realização de audiência exclusivamente para tratativas de conciliação, de forma telepresencial, por meio da plataforma de videoconferência Zoom, nos termos da intimação.

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


# ══════════════════════════════════════════════════
# IMPUGNAÇÃO AOS CÁLCULOS
# ══════════════════════════════════════════════════

def impugnacao_calculos_noronha(
    vara, comarca, processo, reclamante, reclamado, id_despacho,
):
    if id_despacho.strip():
        intro_corpo = f"Em atenção à intimação de ID {id_despacho}, vem"
    else:
        intro_corpo = "Vem"

    return f"""EXCELENTÍSSIMO(A) SENHOR(A) JUIZ(A) DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{_nome(reclamante)}**, por seus advogados signatários, vem, respeitosamente, à Douta e Elevada presença de Vossa Excelência, nos autos da reclamação trabalhista que move em face de **{_nome(reclamado)}**, expor e requerer o que adiante segue:

{intro_corpo} apresentar IMPUGNAÇÃO AOS CÁLCULOS DE LIQUIDAÇÃO apresentados pela reclamada, nos termos do art. 879, §2º, da CLT, conforme razões e demonstrativo em anexo.

Requer seja apreciada a presente impugnação e, acolhidas as razões expostas, seja determinada a retificação dos cálculos para fins de execução.

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


def impugnacao_calculos_parceria(
    vara, comarca, processo, reclamante, reclamado, id_despacho,
):
    if id_despacho.strip():
        intro_corpo = f"Em atenção à intimação de ID {id_despacho}, vem"
    else:
        intro_corpo = "Vem"

    return f"""AO JUÍZO DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{_nome(reclamante)}**, já qualificado nos autos da reclamatória trabalhista promovida em face de **{_nome(reclamado)}**, também já qualificado, vem, respeitosamente, à presença de Vossa Excelência, por meio de seus procuradores, dizer e requerer o que segue:

{intro_corpo} apresentar IMPUGNAÇÃO AOS CÁLCULOS DE LIQUIDAÇÃO apresentados pela reclamada, nos termos do art. 879, §2º, da CLT, conforme razões e demonstrativo em anexo.

Requer seja apreciada a presente impugnação e, acolhidas as razões expostas, seja determinada a retificação dos cálculos para fins de execução.

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


# ══════════════════════════════════════════════════
# CONCORDÂNCIA COM OS CÁLCULOS
# ══════════════════════════════════════════════════

def concordancia_calculos_noronha(
    vara, comarca, processo, reclamante, reclamado, id_despacho,
):
    if id_despacho.strip():
        intro_corpo = f"Em atenção à intimação de ID {id_despacho}, a"
    else:
        intro_corpo = "A"

    return f"""EXCELENTÍSSIMO(A) SENHOR(A) JUIZ(A) DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{_nome(reclamante)}**, por seus advogados signatários, vem, respeitosamente, à Douta e Elevada presença de Vossa Excelência, nos autos da reclamação trabalhista que move em face de **{_nome(reclamado)}**, expor e requerer o que adiante segue:

{intro_corpo} parte reclamante informa que CONCORDA com os cálculos de liquidação apresentados pela reclamada, requerendo a homologação dos valores apurados e o regular prosseguimento do feito executivo.

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""


def concordancia_calculos_parceria(
    vara, comarca, processo, reclamante, reclamado, id_despacho,
):
    if id_despacho.strip():
        intro_corpo = f"Em atenção à intimação de ID {id_despacho}, a"
    else:
        intro_corpo = "A"

    return f"""AO JUÍZO DA {format_juizo(vara, comarca)}

Processo nº {processo}

**{_nome(reclamante)}**, já qualificado nos autos da reclamatória trabalhista promovida em face de **{_nome(reclamado)}**, também já qualificado, vem, respeitosamente, à presença de Vossa Excelência, por meio de seus procuradores, dizer e requerer o que segue:

{intro_corpo} parte reclamante informa que CONCORDA com os cálculos de liquidação apresentados pela reclamada, requerendo a homologação dos valores apurados e o regular prosseguimento do feito executivo.

Termos em que pede deferimento.

Porto Alegre, ___ de __________ de {_ano()}.
"""