import streamlit as st
import streamlit.components.v1 as components
import os
from glob import glob

# Caminhos
html_path = "C:\\Users\\wande\\Documents\\Programação\\streamlit-dashboard_veredas\\output\\2025-07-08\\test_sentinel2_gci_2025-07-083.html"
original_html = "C:\\Users\\wande\\Documents\\Programação\\streamlit-dashboard_veredas\\output\\2025-07-08\\mapa_sentinel2_2025-07-08_naomapeado.html"
kml_folder = "C:\\Users\\wande\\Documents\\Programação\\streamlit-dashboard_veredas\\kml"  # onde os arquivos .kml são salvos

st.set_page_config(page_title="Dashboard de Clusterização", layout="wide")
st.title("Veredas Agronegócios: Clusterizações")

col1, col2 = st.columns(2)
# --- Mostrar HTML ---

with col1:
    st.subheader("🔍 Mapa com Clusterização")
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        components.html(html_content, height=600, width=1200)
    else:
        st.warning("Arquivo HTML de clusterização ainda não gerado.")


with col2:
    st.subheader("🔍 Mapa sem Clusterização")
    if os.path.exists(original_html):
        with open(original_html, 'r', encoding='utf-8') as f:
            components.html(f.read(), height=600)
    else:
        st.error("Arquivo HTML original não encontrado.")


# --- Botão de Atualizar ---
if st.button("🔄 Atualizar visualização"):
    st.rerun()

st.markdown("---")

# --- Mostrar arquivos KML disponíveis ---
st.subheader("Arquivos KML disponíveis para download")

if os.path.isdir(kml_folder):
    kml_files = sorted(glob(os.path.join(kml_folder, "*.kml")), reverse=True)

    if not kml_files:
        st.info("Nenhum arquivo KML encontrado.")
    else:
        for kml_file in kml_files:
            filename = os.path.basename(kml_file)
            with open(kml_file, "rb") as file:
                st.download_button(
                    label=f"📥 Baixar {filename}",
                    data=file,
                    file_name=filename,
                    mime="application/vnd.google-earth.kml+xml"
                )
else:
    st.info(f"Pasta `{kml_folder}` não encontrada.")
