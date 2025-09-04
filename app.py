{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "!pip install streamlit\n",
        "!pip install docx2txt\n",
        "!pip install PyPDF2\n",
        "!pip install sentence_transformers\n",
        "!pip install matplotlib\n",
        "!pip install python-docx"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DIYUaVu4af2C",
        "outputId": "fe03c776-a748-4450-a9c2-d50ab22c4481"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: streamlit in /usr/local/lib/python3.12/dist-packages (1.49.1)\n",
            "Requirement already satisfied: altair!=5.4.0,!=5.4.1,<6,>=4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: blinker<2,>=1.5.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (1.9.0)\n",
            "Requirement already satisfied: cachetools<7,>=4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.5.2)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (8.2.1)\n",
            "Requirement already satisfied: numpy<3,>=1.23 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.0.2)\n",
            "Requirement already satisfied: packaging<26,>=20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (25.0)\n",
            "Requirement already satisfied: pandas<3,>=1.4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.2.2)\n",
            "Requirement already satisfied: pillow<12,>=7.1.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (11.3.0)\n",
            "Requirement already satisfied: protobuf<7,>=3.20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.29.5)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (18.1.0)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.32.4)\n",
            "Requirement already satisfied: tenacity<10,>=8.1.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (8.5.0)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (4.15.0)\n",
            "Requirement already satisfied: watchdog<7,>=2.1.5 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.0.0)\n",
            "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.12/dist-packages (from streamlit) (3.1.45)\n",
            "Requirement already satisfied: pydeck<1,>=0.8.0b4 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.9.1)\n",
            "Requirement already satisfied: tornado!=6.5.0,<7,>=6.0.3 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.4.2)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (3.1.6)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (4.25.1)\n",
            "Requirement already satisfied: narwhals>=1.14.2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (2.2.0)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.12/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.12/dist-packages (from pandas<3,>=1.4.0->streamlit) (2.9.0.post0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.12/dist-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.12/dist-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)\n",
            "Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (3.4.3)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (2.5.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (2025.8.3)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.12/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.2)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.12/dist-packages (from jinja2->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (3.0.2)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (25.3.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (2025.4.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (0.36.2)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (0.27.0)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.12/dist-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.17.0)\n",
            "Requirement already satisfied: docx2txt in /usr/local/lib/python3.12/dist-packages (0.9)\n",
            "Requirement already satisfied: PyPDF2 in /usr/local/lib/python3.12/dist-packages (3.0.1)\n",
            "Requirement already satisfied: sentence_transformers in /usr/local/lib/python3.12/dist-packages (5.1.0)\n",
            "Requirement already satisfied: transformers<5.0.0,>=4.41.0 in /usr/local/lib/python3.12/dist-packages (from sentence_transformers) (4.55.4)\n",
            "Requirement already satisfied: tqdm in /usr/local/lib/python3.12/dist-packages (from sentence_transformers) (4.67.1)\n",
            "Requirement already satisfied: torch>=1.11.0 in /usr/local/lib/python3.12/dist-packages (from sentence_transformers) (2.8.0+cu126)\n",
            "Requirement already satisfied: scikit-learn in /usr/local/lib/python3.12/dist-packages (from sentence_transformers) (1.6.1)\n",
            "Requirement already satisfied: scipy in /usr/local/lib/python3.12/dist-packages (from sentence_transformers) (1.16.1)\n",
            "Requirement already satisfied: huggingface-hub>=0.20.0 in /usr/local/lib/python3.12/dist-packages (from sentence_transformers) (0.34.4)\n",
            "Requirement already satisfied: Pillow in /usr/local/lib/python3.12/dist-packages (from sentence_transformers) (11.3.0)\n",
            "Requirement already satisfied: typing_extensions>=4.5.0 in /usr/local/lib/python3.12/dist-packages (from sentence_transformers) (4.15.0)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.12/dist-packages (from huggingface-hub>=0.20.0->sentence_transformers) (3.19.1)\n",
            "Requirement already satisfied: fsspec>=2023.5.0 in /usr/local/lib/python3.12/dist-packages (from huggingface-hub>=0.20.0->sentence_transformers) (2025.3.0)\n",
            "Requirement already satisfied: packaging>=20.9 in /usr/local/lib/python3.12/dist-packages (from huggingface-hub>=0.20.0->sentence_transformers) (25.0)\n",
            "Requirement already satisfied: pyyaml>=5.1 in /usr/local/lib/python3.12/dist-packages (from huggingface-hub>=0.20.0->sentence_transformers) (6.0.2)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.12/dist-packages (from huggingface-hub>=0.20.0->sentence_transformers) (2.32.4)\n",
            "Requirement already satisfied: hf-xet<2.0.0,>=1.1.3 in /usr/local/lib/python3.12/dist-packages (from huggingface-hub>=0.20.0->sentence_transformers) (1.1.8)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.12/dist-packages (from torch>=1.11.0->sentence_transformers) (75.2.0)\n",
            "Requirement already satisfied: sympy>=1.13.3 in /usr/local/lib/python3.12/dist-packages (from torch>=1.11.0->sentence_transformers) (1.13.3)\n",
            "Requirement already satisfied: networkx in /usr/local/lib/python3.12/dist-packages (from torch>=1.11.0->sentence_transformers) (3.5)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.12/dist-packages (from torch>=1.11.0->sentence_transformers) (3.1.6)\n",
            "Requirement already satisfied: nvidia-cuda-nvrtc-cu12==12.6.77 in /usr/local/lib/python3.12/dist-packages (from torch>=1.11.0->sentence_transformers) (12.6.77)\n",
            "Requirement already satisfied: nvidia-cuda-runtime-cu12==12.6.77 in /usr/local/lib/python3.12/dist-packages (from torch>=1.11.0->sentence_transformers) (12.6.77)\n",
            "Requirement already satisfied: nvidia-cuda-cupti-cu12==12.6.80 in /usr/local/lib/python3.12/dist-packages (from torch>=1.11.0->sentence_transformers) (12.6.80)\n",
            "Requirement already satisfied: nvidia-cudnn-cu12==9.10.2.21 in /usr/local/lib/python3.12/dist-packages (from torch>=1.11.0->sentence_transformers) (9.10.2.21)\n",
            "Requirement already satisfied: nvidia-cublas-cu12==12.6.4.1 in /usr/local/lib/python3.12/dist-packages (from torch>=1.11.0->sentence_transformers) (12.6.4.1)\n",
            "Requirement already satisfied: nvidia-cufft-cu12==11.3.0.4 in /usr/local/lib/python3.12/dist-packages (from torch>=1.11.0->sentence_transformers) (11.3.0.4)\n",
            "Requirement already satisfied: nvidia-curand-cu12==10.3.7.77 in /usr/local/lib/python3.12/dist-packages (from torch>=1.11.0->sentence_transformers) (10.3.7.77)\n",
            "Requirement already satisfied: nvidia-cusolver-cu12==11.7.1.2 in /usr/local/lib/python3.12/dist-packages (from torch>=1.11.0->sentence_transformers) (11.7.1.2)\n",
            "Requirement already satisfied: nvidia-cusparse-cu12==12.5.4.2 in /usr/local/lib/python3.12/dist-packages (from torch>=1.11.0->sentence_transformers) (12.5.4.2)\n",
            "Requirement already satisfied: nvidia-cusparselt-cu12==0.7.1 in /usr/local/lib/python3.12/dist-packages (from torch>=1.11.0->sentence_transformers) (0.7.1)\n",
            "Requirement already satisfied: nvidia-nccl-cu12==2.27.3 in /usr/local/lib/python3.12/dist-packages (from torch>=1.11.0->sentence_transformers) (2.27.3)\n",
            "Requirement already satisfied: nvidia-nvtx-cu12==12.6.77 in /usr/local/lib/python3.12/dist-packages (from torch>=1.11.0->sentence_transformers) (12.6.77)\n",
            "Requirement already satisfied: nvidia-nvjitlink-cu12==12.6.85 in /usr/local/lib/python3.12/dist-packages (from torch>=1.11.0->sentence_transformers) (12.6.85)\n",
            "Requirement already satisfied: nvidia-cufile-cu12==1.11.1.6 in /usr/local/lib/python3.12/dist-packages (from torch>=1.11.0->sentence_transformers) (1.11.1.6)\n",
            "Requirement already satisfied: triton==3.4.0 in /usr/local/lib/python3.12/dist-packages (from torch>=1.11.0->sentence_transformers) (3.4.0)\n",
            "Requirement already satisfied: numpy>=1.17 in /usr/local/lib/python3.12/dist-packages (from transformers<5.0.0,>=4.41.0->sentence_transformers) (2.0.2)\n",
            "Requirement already satisfied: regex!=2019.12.17 in /usr/local/lib/python3.12/dist-packages (from transformers<5.0.0,>=4.41.0->sentence_transformers) (2024.11.6)\n",
            "Requirement already satisfied: tokenizers<0.22,>=0.21 in /usr/local/lib/python3.12/dist-packages (from transformers<5.0.0,>=4.41.0->sentence_transformers) (0.21.4)\n",
            "Requirement already satisfied: safetensors>=0.4.3 in /usr/local/lib/python3.12/dist-packages (from transformers<5.0.0,>=4.41.0->sentence_transformers) (0.6.2)\n",
            "Requirement already satisfied: joblib>=1.2.0 in /usr/local/lib/python3.12/dist-packages (from scikit-learn->sentence_transformers) (1.5.1)\n",
            "Requirement already satisfied: threadpoolctl>=3.1.0 in /usr/local/lib/python3.12/dist-packages (from scikit-learn->sentence_transformers) (3.6.0)\n",
            "Requirement already satisfied: mpmath<1.4,>=1.1.0 in /usr/local/lib/python3.12/dist-packages (from sympy>=1.13.3->torch>=1.11.0->sentence_transformers) (1.3.0)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.12/dist-packages (from jinja2->torch>=1.11.0->sentence_transformers) (3.0.2)\n",
            "Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.12/dist-packages (from requests->huggingface-hub>=0.20.0->sentence_transformers) (3.4.3)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.12/dist-packages (from requests->huggingface-hub>=0.20.0->sentence_transformers) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.12/dist-packages (from requests->huggingface-hub>=0.20.0->sentence_transformers) (2.5.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.12/dist-packages (from requests->huggingface-hub>=0.20.0->sentence_transformers) (2025.8.3)\n",
            "Requirement already satisfied: matplotlib in /usr/local/lib/python3.12/dist-packages (3.10.0)\n",
            "Requirement already satisfied: contourpy>=1.0.1 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (1.3.3)\n",
            "Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (0.12.1)\n",
            "Requirement already satisfied: fonttools>=4.22.0 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (4.59.1)\n",
            "Requirement already satisfied: kiwisolver>=1.3.1 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (1.4.9)\n",
            "Requirement already satisfied: numpy>=1.23 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (2.0.2)\n",
            "Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (25.0)\n",
            "Requirement already satisfied: pillow>=8 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (11.3.0)\n",
            "Requirement already satisfied: pyparsing>=2.3.1 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (3.2.3)\n",
            "Requirement already satisfied: python-dateutil>=2.7 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (2.9.0.post0)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.12/dist-packages (from python-dateutil>=2.7->matplotlib) (1.17.0)\n",
            "Collecting python-docx\n",
            "  Downloading python_docx-1.2.0-py3-none-any.whl.metadata (2.0 kB)\n",
            "Requirement already satisfied: lxml>=3.1.0 in /usr/local/lib/python3.12/dist-packages (from python-docx) (5.4.0)\n",
            "Requirement already satisfied: typing_extensions>=4.9.0 in /usr/local/lib/python3.12/dist-packages (from python-docx) (4.15.0)\n",
            "Downloading python_docx-1.2.0-py3-none-any.whl (252 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m253.0/253.0 kB\u001b[0m \u001b[31m5.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: python-docx\n",
            "Successfully installed python-docx-1.2.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "id": "8vmGVEpyaTad"
      },
      "outputs": [],
      "source": [
        "import streamlit as st\n",
        "import os\n",
        "import PyPDF2\n",
        "import matplotlib.pyplot as plt\n",
        "from sentence_transformers import SentenceTransformer\n",
        "from sklearn.metrics.pairwise import cosine_similarity"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def extract_text_from_pdf(file):\n",
        "    text = \"\"\n",
        "    reader = PyPDF2.PdfReader(file)\n",
        "    for page in reader.pages:\n",
        "        if page.extract_text():\n",
        "            text += page.extract_text() + \" \"\n",
        "    return text.strip()\n",
        "\n",
        "def extract_text_from_docx(file):\n",
        "    doc = docx.Document(file)\n",
        "    return \" \".join([para.text for para in doc.paragraphs]).strip()\n",
        "\n",
        "def load_resume(file):\n",
        "    if file.name.endswith(\".pdf\"):\n",
        "        return extract_text_from_pdf(file)\n",
        "    elif file.name.endswith(\".docx\"):\n",
        "        return extract_text_from_docx(file)\n",
        "    else:\n",
        "        return None"
      ],
      "metadata": {
        "id": "1ErQ0oScabjx"
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def analyze_skills(resume_text, skills):\n",
        "    matched, missing = [], []\n",
        "    text_lower = resume_text.lower()\n",
        "    for skill in skills:\n",
        "        if skill.lower() in text_lower:\n",
        "            matched.append(skill)\n",
        "        else:\n",
        "            missing.append(skill)\n",
        "    return matched, missing\n"
      ],
      "metadata": {
        "id": "XtYqiB9FbeZr"
      },
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "st.title(\"📄 AI Resume Screening System\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RBE176Q9bh_R",
        "outputId": "f12bfa79-2ed7-49b2-ecfa-3f5e0e318abe"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2025-09-03 11:54:48.869 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 11:54:49.685 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.12/dist-packages/colab_kernel_launcher.py [ARGUMENTS]\n",
            "2025-09-03 11:54:49.688 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 11:54:49.689 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DeltaGenerator()"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "jd_text = st.text_area(\"Paste Job Description here:\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8vf64xFQbiW9",
        "outputId": "8bc38f1c-bf71-4f15-9957-32f1858fe93d"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2025-09-03 11:55:03.769 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 11:55:03.770 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 11:55:03.771 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 11:55:03.772 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 11:55:03.773 Session state does not function when running a script without `streamlit run`\n",
            "2025-09-03 11:55:03.774 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 11:55:03.775 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 11:55:03.776 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "uploaded_files = st.file_uploader(\"Upload Resumes (PDF/DOCX)\", type=[\"pdf\", \"docx\"], accept_multiple_files=True)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mUHviuxHbmAO",
        "outputId": "173b5cd8-57cd-4de9-de55-890a622d7e7e"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2025-09-03 11:55:25.364 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 11:55:25.365 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 11:55:25.366 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 11:55:25.368 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 11:55:25.369 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 11:55:25.370 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "skills = [\"Python\", \"SQL\", \"Excel\", \"Power BI\", \"Tableau\",\n",
        "          \"Machine Learning\", \"Statistics\", \"Communication\", \"Problem Solving\"]\n",
        "\n",
        "results = [] # Initialize results list here\n",
        "\n",
        "if st.button(\"Process Resumes\"):\n",
        "    if not jd_text:\n",
        "        st.warning(\"Please paste a Job Description first!\")\n",
        "    elif not uploaded_files:\n",
        "        st.warning(\"Please upload at least one resume!\")\n",
        "    else:\n",
        "        model = SentenceTransformer(\"all-MiniLM-L6-v2\")\n",
        "\n",
        "        jd_embedding = model.encode(jd_text)\n",
        "\n",
        "        # results = [] # Moved initialization outside the if block\n",
        "\n",
        "        for file in uploaded_files:\n",
        "            resume_text = load_resume(file)\n",
        "            if not resume_text:\n",
        "                continue\n",
        "\n",
        "            resume_embedding = model.encode(resume_text)\n",
        "            score = cosine_similarity([jd_embedding], [resume_embedding])[0][0] * 100\n",
        "\n",
        "            matched, missing = analyze_skills(resume_text, skills)\n",
        "\n",
        "            results.append({\n",
        "                \"name\": file.name,\n",
        "                \"score\": round(score, 2),\n",
        "                \"matched\": matched,\n",
        "                \"missing\": missing\n",
        "            })"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "axZuC-hdbrRc",
        "outputId": "72f96f51-d5c7-41f4-b085-79a27b8ae6e5"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2025-09-03 11:57:09.432 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 11:57:09.436 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 11:57:09.438 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 11:57:09.439 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 11:57:09.442 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 11:57:09.443 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "results = sorted(results, key=lambda x: x[\"score\"], reverse=True)\n"
      ],
      "metadata": {
        "id": "EUZycW7Zb6a4"
      },
      "execution_count": 14,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Show results\n",
        "st.subheader(\"🏆 Ranked Candidates\")\n",
        "for r in results:\n",
        "    st.write(f\"**{r['name']}** - {r['score']}% match\")\n",
        "    st.write(f\"✅ Matched: {', '.join(r['matched']) if r['matched'] else 'None'}\")\n",
        "    st.write(f\"❌ Missing: {', '.join(r['missing']) if r['missing'] else 'None'}\")\n",
        "    st.markdown(\"---\")\n",
        "\n",
        "# Plot Top 5\n",
        "top5 = results[:5]\n",
        "if top5:\n",
        "    fig, ax = plt.subplots()\n",
        "    ax.barh([r[\"name\"] for r in top5], [r[\"score\"] for r in top5])\n",
        "    st.pyplot(fig) # Added this line to display the plot in Streamlit"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "79TffCaWcAOg",
        "outputId": "c339e2c5-a898-4437-9c62-d273cb2725e5"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2025-09-03 11:58:36.070 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 11:58:36.072 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 11:58:36.073 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ]
    }
  ]
}