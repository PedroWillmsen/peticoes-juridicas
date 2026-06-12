import streamlit as st
from wordGenerator import gerar_docx
from claude_extractor import gerar_peticao_com_claude

st.set_page_config(page_title="Petições | ES & MF", layout="centered")

def check_password():
    if st.session_state.get("autenticado"):
        return True
    st.title("⚖️ Gerador de Petições")
    st.subheader("Entrar na sua conta")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        senha = st.text_input("Senha", type="password", placeholder="••••••••")
        if st.button("Entrar", type="primary", use_container_width=True):
            if senha == st.secrets["APP_PASSWORD"]:
                st.session_state.autenticado = True
                st.rerun()
            else:
                st.error("❌ Senha incorreta.")
    return False

if not check_password():
    st.stop()

col1, col2 = st.columns([4, 1])
with col1:
    st.title("⚖️ Gerador de Petições")
with col2:
    st.write("")
    if st.button("Sair", use_container_width=True):
        st.session_state.autenticado = False
        st.rerun()

st.divider()

modelo = st.radio(
    "Modelo do escritório",
    ["Parceria Marília + Eleandro", "Noronha"],
    horizontal=True,
)
st.divider()

st.subheader("📎 Prints do processo")
uploaded_files = st.file_uploader(
    "Adicione os prints (PROMAD, PJe ou qualquer print do processo)",
    type=["png", "jpg", "jpeg"],
    accept_multiple_files=True,
    key="uploads",
)

observacao = st.text_area(
    "💬 Observações (opcional)",
    placeholder="Ex: apresentar dados bancários para o alvará / juntar documentos de rescisão...",
    height=100,
)
st.divider()

if st.button("🧠 Gerar Petição com IA", type="primary", use_container_width=True):
    if not uploaded_files and not observacao.strip():
        st.error("❌ Adicione prints ou escreva uma observação.")
        st.stop()

    with st.spinner("🤖 Claude está lendo os prints e escrevendo a petição..."):
        try:
            imagens = []
            for f in uploaded_files:
                ext = f.name.lower().split(".")[-1]
                mt = "image/jpeg" if ext in ["jpg", "jpeg"] else f"image/{ext}"
                imagens.append((f.read(), mt))

            texto_gerado = gerar_peticao_com_claude(imagens, observacao, modelo)

            nome = "peticao.docx"
            gerar_docx(texto_gerado, modelo=modelo, nome_arquivo=nome)

            with open(nome, "rb") as f:
                st.download_button(
                    label="📥 Baixar petição (.docx)",
                    data=f,
                    file_name="peticao_gerada.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    use_container_width=True,
                )

            st.success("✅ Petição gerada com sucesso!")
            with st.expander("👁️ Ver texto gerado"):
                st.text(texto_gerado)

        except Exception as e:
            st.error(f"❌ Erro: {e}")
            raise e
