import streamlit as st
from supabase_client import get_client
from wordGenerator import gerar_docx
from claude_extractor import gerar_peticao_com_claude

st.set_page_config(page_title="Petições | ES & MF", layout="centered")

if "user" not in st.session_state:
    st.session_state.user = None
if "session" not in st.session_state:
    st.session_state.session = None


def pagina_login():
    st.title("⚖️ Gerador de Petições")
    st.subheader("Entrar na sua conta")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        email = st.text_input("E-mail", placeholder="seu@email.com")
        senha = st.text_input("Senha", type="password", placeholder="••••••••")

        if st.button("Entrar", type="primary", use_container_width=True):
            if not email or not senha:
                st.error("Preencha e-mail e senha.")
                return
            try:
                client = get_client()
                response = client.auth.sign_in_with_password({
                    "email": email,
                    "password": senha,
                })
                st.session_state.user = response.user
                st.session_state.session = response.session
                st.success("✅ Login realizado!")
                st.rerun()
            except Exception as e:
                st.error(f"❌ Erro: {e}")

        st.caption("Não tem conta? Entre em contato com o administrador.")


def pagina_principal():
    col1, col2 = st.columns([4, 1])
    with col1:
        st.title("⚖️ Gerador de Petições")
    with col2:
        st.write("")
        if st.button("Sair", use_container_width=True):
            try:
                client = get_client()
                client.auth.sign_out()
            except Exception:
                pass
            st.session_state.user = None
            st.session_state.session = None
            st.rerun()

    email_usuario = st.session_state.user.email if st.session_state.user else ""
    st.caption(f"Conectado como: {email_usuario}")
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


if st.session_state.user is None:
    pagina_login()
else:
    pagina_principal()