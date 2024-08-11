{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "mount_file_id": "1KLqViBkke_DBA-nZ44OEduTKrevQAvmv",
      "authorship_tag": "ABX9TyPfbDQEvQh6UOYtQiqWMJJG",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/FayezAltawafshih/Data-Analyst-with-Python/blob/main/Health_Insurance_projects.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install streamlit"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rQLhmVS5aKvk",
        "outputId": "9d9ae584-3b6e-4b04-f061-58de8a2fad89"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting streamlit\n",
            "  Downloading streamlit-1.37.1-py2.py3-none-any.whl.metadata (8.5 kB)\n",
            "Requirement already satisfied: altair<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.2.2)\n",
            "Requirement already satisfied: blinker<2,>=1.0.0 in /usr/lib/python3/dist-packages (from streamlit) (1.4)\n",
            "Requirement already satisfied: cachetools<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (5.4.0)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.1.7)\n",
            "Requirement already satisfied: numpy<3,>=1.20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (1.26.4)\n",
            "Requirement already satisfied: packaging<25,>=20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (24.1)\n",
            "Requirement already satisfied: pandas<3,>=1.3.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.1.4)\n",
            "Requirement already satisfied: pillow<11,>=7.1.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (9.4.0)\n",
            "Requirement already satisfied: protobuf<6,>=3.20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (3.20.3)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (14.0.2)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.32.3)\n",
            "Requirement already satisfied: rich<14,>=10.14.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (13.7.1)\n",
            "Collecting tenacity<9,>=8.1.0 (from streamlit)\n",
            "  Downloading tenacity-8.5.0-py3-none-any.whl.metadata (1.2 kB)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.10/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.3.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.12.2)\n",
            "Collecting gitpython!=3.1.19,<4,>=3.0.7 (from streamlit)\n",
            "  Downloading GitPython-3.1.43-py3-none-any.whl.metadata (13 kB)\n",
            "Collecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
            "  Downloading pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)\n",
            "Requirement already satisfied: tornado<7,>=6.0.3 in /usr/local/lib/python3.10/dist-packages (from streamlit) (6.3.3)\n",
            "Collecting watchdog<5,>=2.1.5 (from streamlit)\n",
            "  Downloading watchdog-4.0.2-py3-none-manylinux2014_x86_64.whl.metadata (38 kB)\n",
            "Requirement already satisfied: entrypoints in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.4)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (3.1.4)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.12.1)\n",
            "Collecting gitdb<5,>=4.0.1 (from gitpython!=3.1.19,<4,>=3.0.7->streamlit)\n",
            "  Downloading gitdb-4.0.11-py3-none-any.whl.metadata (1.2 kB)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.3.0->streamlit) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.3.0->streamlit) (2024.1)\n",
            "Requirement already satisfied: tzdata>=2022.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.3.0->streamlit) (2024.1)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (3.7)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (2.0.7)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (2024.7.4)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (2.16.1)\n",
            "Collecting smmap<6,>=3.0.1 (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit)\n",
            "  Downloading smmap-5.0.1-py3-none-any.whl.metadata (4.3 kB)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.5)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (24.2.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.12.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.35.1)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.20.0)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas<3,>=1.3.0->streamlit) (1.16.0)\n",
            "Downloading streamlit-1.37.1-py2.py3-none-any.whl (8.7 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m8.7/8.7 MB\u001b[0m \u001b[31m60.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading GitPython-3.1.43-py3-none-any.whl (207 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m207.3/207.3 kB\u001b[0m \u001b[31m16.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m84.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading tenacity-8.5.0-py3-none-any.whl (28 kB)\n",
            "Downloading watchdog-4.0.2-py3-none-manylinux2014_x86_64.whl (82 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m82.9/82.9 kB\u001b[0m \u001b[31m6.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading gitdb-4.0.11-py3-none-any.whl (62 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m62.7/62.7 kB\u001b[0m \u001b[31m4.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading smmap-5.0.1-py3-none-any.whl (24 kB)\n",
            "Installing collected packages: watchdog, tenacity, smmap, pydeck, gitdb, gitpython, streamlit\n",
            "  Attempting uninstall: tenacity\n",
            "    Found existing installation: tenacity 9.0.0\n",
            "    Uninstalling tenacity-9.0.0:\n",
            "      Successfully uninstalled tenacity-9.0.0\n",
            "Successfully installed gitdb-4.0.11 gitpython-3.1.43 pydeck-0.9.1 smmap-5.0.1 streamlit-1.37.1 tenacity-8.5.0 watchdog-4.0.2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "\n",
        "config = {\n",
        "    \"include_colab_link\": True,\n",
        "    \"title\": \"Health Insurance Project\"\n",
        "}\n",
        "\n",
        "# Access the title using the correct key\n",
        "st.title(config[\"title\"])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LV-oWExTashB",
        "outputId": "e7c1b92a-4109-43e0-97ad-c5e1609b6505"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2024-08-11 21:50:42.204 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.10/dist-packages/colab_kernel_launcher.py [ARGUMENTS]\n"
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
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Importing Libraries\n",
        "import numpy as np\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.linear_model import LinearRegression\n",
        "from sklearn.metrics import mean_squared_error, r2_score\n"
      ],
      "metadata": {
        "id": "xJasNQVa0oLv",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0ffb01cc-87e3-42b2-a4e4-16c942a18176"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: streamlit in /usr/local/lib/python3.10/dist-packages (1.37.1)\n",
            "Requirement already satisfied: altair<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.2.2)\n",
            "Requirement already satisfied: blinker<2,>=1.0.0 in /usr/lib/python3/dist-packages (from streamlit) (1.4)\n",
            "Requirement already satisfied: cachetools<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (5.4.0)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.1.7)\n",
            "Requirement already satisfied: numpy<3,>=1.20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (1.26.4)\n",
            "Requirement already satisfied: packaging<25,>=20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (24.1)\n",
            "Requirement already satisfied: pandas<3,>=1.3.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.1.4)\n",
            "Requirement already satisfied: pillow<11,>=7.1.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (9.4.0)\n",
            "Requirement already satisfied: protobuf<6,>=3.20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (3.20.3)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (14.0.2)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.32.3)\n",
            "Requirement already satisfied: rich<14,>=10.14.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (13.7.1)\n",
            "Requirement already satisfied: tenacity<9,>=8.1.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.5.0)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.10/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.3.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.12.2)\n",
            "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.10/dist-packages (from streamlit) (3.1.43)\n",
            "Requirement already satisfied: pydeck<1,>=0.8.0b4 in /usr/local/lib/python3.10/dist-packages (from streamlit) (0.9.1)\n",
            "Requirement already satisfied: tornado<7,>=6.0.3 in /usr/local/lib/python3.10/dist-packages (from streamlit) (6.3.3)\n",
            "Requirement already satisfied: watchdog<5,>=2.1.5 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.0.2)\n",
            "Requirement already satisfied: entrypoints in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.4)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (3.1.4)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.12.1)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.10/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.11)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.3.0->streamlit) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.3.0->streamlit) (2024.1)\n",
            "Requirement already satisfied: tzdata>=2022.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.3.0->streamlit) (2024.1)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (3.7)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (2.0.7)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (2024.7.4)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (2.16.1)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.10/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.1)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.5)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (24.2.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.12.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.35.1)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.20.0)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas<3,>=1.3.0->streamlit) (1.16.0)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Data Collection & Analyst**"
      ],
      "metadata": {
        "id": "eTx19wQR4olu"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# loading the data frm csv\n",
        "insurance_dataset = pd.read_csv('/content/drive/MyDrive/insurance.csv')"
      ],
      "metadata": {
        "id": "zyvX3yhk4uIh"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# first 5 rows\n",
        "insurance_dataset.head(5)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "3p2sdaFa4_Ts",
        "outputId": "85942708-1588-4e23-da60-d9de92211c65"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   age     sex     bmi  children smoker     region      charges\n",
              "0   19  female  27.900         0    yes  southwest  16884.92400\n",
              "1   18    male  33.770         1     no  southeast   1725.55230\n",
              "2   28    male  33.000         3     no  southeast   4449.46200\n",
              "3   33    male  22.705         0     no  northwest  21984.47061\n",
              "4   32    male  28.880         0     no  northwest   3866.85520"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-2e41d5b1-3a8c-40e4-a6cb-37090cacddad\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>age</th>\n",
              "      <th>sex</th>\n",
              "      <th>bmi</th>\n",
              "      <th>children</th>\n",
              "      <th>smoker</th>\n",
              "      <th>region</th>\n",
              "      <th>charges</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>19</td>\n",
              "      <td>female</td>\n",
              "      <td>27.900</td>\n",
              "      <td>0</td>\n",
              "      <td>yes</td>\n",
              "      <td>southwest</td>\n",
              "      <td>16884.92400</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>18</td>\n",
              "      <td>male</td>\n",
              "      <td>33.770</td>\n",
              "      <td>1</td>\n",
              "      <td>no</td>\n",
              "      <td>southeast</td>\n",
              "      <td>1725.55230</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>28</td>\n",
              "      <td>male</td>\n",
              "      <td>33.000</td>\n",
              "      <td>3</td>\n",
              "      <td>no</td>\n",
              "      <td>southeast</td>\n",
              "      <td>4449.46200</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>33</td>\n",
              "      <td>male</td>\n",
              "      <td>22.705</td>\n",
              "      <td>0</td>\n",
              "      <td>no</td>\n",
              "      <td>northwest</td>\n",
              "      <td>21984.47061</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>32</td>\n",
              "      <td>male</td>\n",
              "      <td>28.880</td>\n",
              "      <td>0</td>\n",
              "      <td>no</td>\n",
              "      <td>northwest</td>\n",
              "      <td>3866.85520</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-2e41d5b1-3a8c-40e4-a6cb-37090cacddad')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-2e41d5b1-3a8c-40e4-a6cb-37090cacddad button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-2e41d5b1-3a8c-40e4-a6cb-37090cacddad');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-a2014b09-611b-4d57-93b4-41116fe7b16e\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-a2014b09-611b-4d57-93b4-41116fe7b16e')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-a2014b09-611b-4d57-93b4-41116fe7b16e button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "insurance_dataset",
              "summary": "{\n  \"name\": \"insurance_dataset\",\n  \"rows\": 1338,\n  \"fields\": [\n    {\n      \"column\": \"age\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 14,\n        \"min\": 18,\n        \"max\": 64,\n        \"num_unique_values\": 47,\n        \"samples\": [\n          21,\n          45,\n          36\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"sex\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"male\",\n          \"female\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"bmi\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 6.098186911679014,\n        \"min\": 15.96,\n        \"max\": 53.13,\n        \"num_unique_values\": 548,\n        \"samples\": [\n          23.18,\n          26.885\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"children\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1,\n        \"min\": 0,\n        \"max\": 5,\n        \"num_unique_values\": 6,\n        \"samples\": [\n          0,\n          1\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"smoker\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"no\",\n          \"yes\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"region\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 4,\n        \"samples\": [\n          \"southeast\",\n          \"northeast\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"charges\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 12110.011236694001,\n        \"min\": 1121.8739,\n        \"max\": 63770.42801,\n        \"num_unique_values\": 1337,\n        \"samples\": [\n          8688.85885,\n          5708.867\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Number of rows and coulmns\n",
        "insurance_dataset.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Nkl_W7h-4fFZ",
        "outputId": "3126d95c-02d5-411b-8d9a-6502dc0cdc7a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(1338, 7)"
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# getting some basic information about the datases\n",
        "insurance_dataset.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ai_8hJHn7E3S",
        "outputId": "7ec37cab-a649-4059-cd64-787aff81b017"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 1338 entries, 0 to 1337\n",
            "Data columns (total 7 columns):\n",
            " #   Column    Non-Null Count  Dtype  \n",
            "---  ------    --------------  -----  \n",
            " 0   age       1338 non-null   int64  \n",
            " 1   sex       1338 non-null   object \n",
            " 2   bmi       1338 non-null   float64\n",
            " 3   children  1338 non-null   int64  \n",
            " 4   smoker    1338 non-null   object \n",
            " 5   region    1338 non-null   object \n",
            " 6   charges   1338 non-null   float64\n",
            "dtypes: float64(2), int64(2), object(3)\n",
            "memory usage: 73.3+ KB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Categorical Features** :\n",
        "- Sex\n",
        "- Smoker\n",
        "- Region"
      ],
      "metadata": {
        "id": "w4LyRmXK-xQO"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# cheking for missing value\n",
        "insurance_dataset.isnull().sum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 304
        },
        "id": "jTOFQpWR_NIK",
        "outputId": "b533f542-823d-4d1c-d9dc-8256bf5f4d3b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "age         0\n",
              "sex         0\n",
              "bmi         0\n",
              "children    0\n",
              "smoker      0\n",
              "region      0\n",
              "charges     0\n",
              "dtype: int64"
            ],
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>0</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>age</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>sex</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>bmi</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>children</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>smoker</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>region</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>charges</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div><br><label><b>dtype:</b> int64</label>"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Data Analysis using Charts **"
      ],
      "metadata": {
        "id": "SgKFOCez_0K8"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# statistical mesures of the dataset\n",
        "insurance_dataset.describe()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 300
        },
        "id": "wbhJJIEE_5Pz",
        "outputId": "54f57994-d8b6-4969-fde0-3f00d979cb4a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "               age          bmi     children       charges\n",
              "count  1338.000000  1338.000000  1338.000000   1338.000000\n",
              "mean     39.207025    30.663397     1.094918  13270.422265\n",
              "std      14.049960     6.098187     1.205493  12110.011237\n",
              "min      18.000000    15.960000     0.000000   1121.873900\n",
              "25%      27.000000    26.296250     0.000000   4740.287150\n",
              "50%      39.000000    30.400000     1.000000   9382.033000\n",
              "75%      51.000000    34.693750     2.000000  16639.912515\n",
              "max      64.000000    53.130000     5.000000  63770.428010"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-a749eff6-0113-4863-8d52-d72dbba8fd47\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>age</th>\n",
              "      <th>bmi</th>\n",
              "      <th>children</th>\n",
              "      <th>charges</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>1338.000000</td>\n",
              "      <td>1338.000000</td>\n",
              "      <td>1338.000000</td>\n",
              "      <td>1338.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>39.207025</td>\n",
              "      <td>30.663397</td>\n",
              "      <td>1.094918</td>\n",
              "      <td>13270.422265</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>14.049960</td>\n",
              "      <td>6.098187</td>\n",
              "      <td>1.205493</td>\n",
              "      <td>12110.011237</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>18.000000</td>\n",
              "      <td>15.960000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1121.873900</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>27.000000</td>\n",
              "      <td>26.296250</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>4740.287150</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>39.000000</td>\n",
              "      <td>30.400000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>9382.033000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>51.000000</td>\n",
              "      <td>34.693750</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>16639.912515</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>64.000000</td>\n",
              "      <td>53.130000</td>\n",
              "      <td>5.000000</td>\n",
              "      <td>63770.428010</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-a749eff6-0113-4863-8d52-d72dbba8fd47')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-a749eff6-0113-4863-8d52-d72dbba8fd47 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-a749eff6-0113-4863-8d52-d72dbba8fd47');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-3b2f7f8f-7ae0-4e7c-bc51-27f25e29cb22\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-3b2f7f8f-7ae0-4e7c-bc51-27f25e29cb22')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-3b2f7f8f-7ae0-4e7c-bc51-27f25e29cb22 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "summary": "{\n  \"name\": \"insurance_dataset\",\n  \"rows\": 8,\n  \"fields\": [\n    {\n      \"column\": \"age\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 460.6106090399993,\n        \"min\": 14.049960379216154,\n        \"max\": 1338.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          39.20702541106129,\n          39.0,\n          1338.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"bmi\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 463.29524977918294,\n        \"min\": 6.098186911679014,\n        \"max\": 1338.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          30.66339686098655,\n          30.4,\n          1338.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"children\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 472.5368318870757,\n        \"min\": 0.0,\n        \"max\": 1338.0,\n        \"num_unique_values\": 7,\n        \"samples\": [\n          1338.0,\n          1.0949177877429,\n          2.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"charges\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 20381.922846226596,\n        \"min\": 1121.8739,\n        \"max\": 63770.42801,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          13270.422265141257,\n          9382.033,\n          1338.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# distribution of  age value\n",
        "sns.set()\n",
        "plt.figure(figsize=(6,6))\n",
        "sns.distplot(insurance_dataset['age'])\n",
        "plt.title('Age Distribution')\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 764
        },
        "id": "zRDRQUEf7keL",
        "outputId": "76245bfc-8b12-4e08-ef38-043180038267"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-8-45f6d2dc5c10>:4: UserWarning: \n",
            "\n",
            "`distplot` is a deprecated function and will be removed in seaborn v0.14.0.\n",
            "\n",
            "Please adapt your code to use either `displot` (a figure-level function with\n",
            "similar flexibility) or `histplot` (an axes-level function for histograms).\n",
            "\n",
            "For a guide to updating your code to use the new functions, please see\n",
            "https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751\n",
            "\n",
            "  sns.distplot(insurance_dataset['age'])\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 600x600 with 1 Axes>"
            ],
            "image/png": "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oaqqplWhRq1SYNiAnl2+pUZOr39bsP6sf3euP9B1nwM/P0+7BwrLd7I6ERERdSsMNURERCQLDDVEREQkCww1REREJAsMNURERCQLDDVEREQkCww1REREJAsMNURERCQLDDVEREQkCww1REREJAsMNURERCQLDDVEREQkCww1REREJAsMNURERCQLDDVEREQkCww1REREJAsMNURERCQLDDVEREQkCww1REREJAsMNURERCQLDDVEREQkCww1REREJAsMNURERCQLDDVEREQkCww1REREJAsMNURERCQLDDVEREQkCww1REREJAsMNURERCQLDDVEREQkCww1REREJAsMNURERCQLDDVEREQkCww1REREJAsMNURERCQLDDVEREQkCww1REREJAsMNURERCQLDDVEREQkCww1REREJAsMNURERCQLDDVEREQkCy4XajIyMjB37lzExcUhISEBy5Ytg9FovOZxkiRh9erVmDBhAmJjYzFr1iwcPXrUZp9jx45h7ty5SEhIQHR0NCZMmIBnn30WBQUFNvulpaUhMjKy0dfGjRsdWVUiIiJyIKWzC3AlnU6H5ORk9OvXD2lpaSgoKMDLL78Mg8GAF154ocVj16xZg+XLl2PhwoWIjIzEhg0bMG/ePHz22WcIDQ0FAOj1eoSHh+POO++Ev78/Ll68iDfffBPHjx/H5s2boVarrefTaDRYt26dzTUazkNERESux6VCzaZNm1BZWYkVK1bAx8cHAGA2m7F48WKkpKQgMDCwyeNqamqwatUqzJs3D3PmzAEAjBw5ElOnTkV6ejoWLVoEABg3bhzGjRtnPS4+Ph5BQUGYN28eTpw4gREjRlgfE0URcXFxHVFNIiIi6gAu1f20b98+jB071hpoACApKQkWiwX79+9v9rjDhw+joqICSUlJ1m1qtRqTJ0/Gvn37Wrxmw7VMJlO7yk5ERETO5VKhJjMzE+Hh4TbbtFotAgICkJmZ2eJxABodGxERgby8PBgMBpvtZrMZRqMRGRkZePXVVzF06FCMHDnSZh+DwYAxY8ZgyJAhmDZtGj744IP2VI2IiIg6mEt1P+n1emi12kbbvb29odPpWjxOrVbDzc3NZrtWq4UkSdDpdNBoNNbt9957Lw4fPgwAiI6OxurVq6FU/v5UhIWFYeHChRgyZAhqamqwZcsWPP/88ygvL8f8+fPb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PjZ06FAMHToUAGT9+s+fPx/x8fGIjIwEAHz55Zf44IMPcP/99yMgIACAvOt/0003ISYmBo8//jgWLFgANzc3rF69Gmq1Gvfccw8A+b7/r7RlyxYEBwdj5MiRjR6T8+sPAIIkNbHkLHVZOTk51ul7V3v33Xetv/Q//PBDrFmzBnl5eejfvz+efPJJ3HjjjZ1Z1A4xceJE5ObmNvnYl19+af1LTK71X716NbZt24YLFy5AkiT06dMHkydPxvz5821mA3355Zd4/fXXkZWVheDgYDz00EOYOXOmE0veMQ4dOoT7778fH330EWJiYqzb5fr6L126FN9++y0uXboEi8WCfv364c4778R9990HQRCs+8m1/gBQUlKCl156CV999RVMJhNGjRqFZ555xqZrSs7vf51Oh4SEBCQnJ+Opp55qch85v/4MNURERCQLHFNDREREssBQQ0RERLLAUENERESywFBDREREssBQQ0RERLLAUENERESywFBDREREssBQQ0RERLLAUENERESywFBDREREssBQQ0RERLLAUENEspGbm4tFixZhypQpiI2NRXx8PB5//HHk5OQ02vfUqVO49957ERsbi8TERLz55pvYvHkzIiMjG+3/zTff4J577kFcXByGDx+Ohx56CGfPnu2sahGRnXhDSyKSjR07dmDlypWYNGkSevfujdzcXGzcuBFeXl744osv4O7uDgAoKCjA7bffDgC477774OHhgQ8//BBqtRqnTp2yuaP7p59+iqeffhrjxo3DhAkTUF1djY0bN6K8vByffPKJdT8icj6GGiKSDYPBAI1GY7Pt6NGjmDVrFl555RXccccdAIClS5fiv//9Lz755BNERUUBAMrKyjBlyhSUlZVZQ01lZSUmTJiAqVOnYsmSJdZzFhUVYerUqUhKSrLZTkTOxe4nIpKNKwONyWRCaWkpwsLCoNVqcfLkSetj3377LeLi4qyBBgB8fHxw22232ZzvwIED0Ov1uOWWW1BSUmL9EkURw4YNw6FDhzq+UkRkN6WzC0BE5CgGgwGrVq3Cxx9/jIKCAlzZEF1eXm79d25uLuLi4hodHxYWZvPz+fPnAQDJyclNXs/Ly6v9hSYih2GoISLZWLJkCT7++GMkJycjLi4OPXr0gCAIWLBgAdrS095wzLJlyxAQENDocYVC0e4yE5HjMNQQkWzs3LkTd9xxB55++mnrtpqaGptWGgDo06cPsrOzGx1/4cIFm59DQ0MBAP7+/rj++us7oMRE5EgcU0NEstFUy8n69ethNpttto0bNw5Hjx7Fb7/9Zt1WVlaGLVu22Ow3fvx4eHl5YdWqVTCZTI3OXVJS4qCSE5EjsKWGiGRjwoQJ+Oyzz+Dl5YUBAwbg6NGjOHDgAHx8fGz2e+CBB/D5559j7ty5uPfee61TuoOCglBWVgZBEADUjZlZtGgR/vrXv2LGjBmYNm0a/Pz8kJeXh2+++QYjRozACy+84ISaElFTGGqISDaee+45iKKILVu2oKamBiNGjMB//vMfPPDAAzb7BQUF4d1338XSpUuxatUq+Pn54U9/+hPc3d2xdOlSuLm5Wfe97bbb0KtXL6xevRrp6ekwGo0IDAzEqFGjMGPGjM6uIhG1gOvUEBHV+8c//oH3338fR44c4SBgoi6IY2qIqFsyGAw2P5eWluLzzz/HyJEjGWiIuih2PxFRtzRr1iyMHj0aERERKCoqwubNm1FRUYH/+Z//cXbRiKiN2P1ERN3Sv/71L+zcuROXLl2CIAgYMmQIHn30UU7dJurCGGqIiIhIFjimhoiIiGSBoYaIiIhkgaGGiIiIZIGhhoiIiGSBoYaIiIhkgaGGiIiIZIGhhoiIiGSBoYaIiIhkgaGGiIiIZOH/AwSzPE4MPkxCAAAAAElFTkSuQmCC\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Gender Columns\n",
        "plt.figure(figsize=(7,7))\n",
        "sns.countplot(x='sex',data=insurance_dataset)\n",
        "plt.title('Sex Distribution')\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 650
        },
        "id": "g2O1s4w7B2tC",
        "outputId": "c703ebb4-16a5-4f79-d74c-78018bfbe58d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 700x700 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAnQAAAJ5CAYAAAAn960RAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAABAPElEQVR4nO3de1iUdeL//xdHV42BcNFWwQQMMgWhXJGFaD18JdDUrSjX1F0zzcoDbpbmqotmagdXE80U7WBalodtXSXTykSJta0sM0tTsNBNrcwZPBSHmd8f/piPs3hAjvPG5+O6uta57/fc875b576e3fc9Mx4Oh8MhAAAAGMuzvicAAACA6iHoAAAADEfQAQAAGI6gAwAAMBxBBwAAYDiCDgAAwHAEHQAAgOEIOgAAAMMRdAAAAIYj6ACgErp166YJEybU+uscOnRIkZGRWrt2rXPZhAkTFBsbW+uvXS4yMlKZmZl19noAqs+7vicA4Mqwd+9eLViwQJ9//rl++OEHBQQEqG3bturWrZsGDRpUp3MZNGiQPvzwQ0mSh4eHmjRpoqCgIEVHR6tfv35KSEiokdfZunWrdu3apVGjRtXI9mqSO88NwOUj6ADUuk8++USDBw9Wy5YtlZaWpqCgIH333Xf67LPPtGzZsjoPOkm65ppr9Je//EWSdObMGX3zzTfavHmz1q1bp5SUFD399NPy8fFxjt+4caM8PDwu6zW2bt2qFStWXFY0tWrVSrt27ZK3d+0eni82t127dsnLy6tWXx9AzSLoANS6559/Xn5+flq9erUsFovLuh9//LFe5uTn56e+ffu6LBs3bpymT5+uV199Va1atdIjjzziXOfr61ur8yktLZXdbpevr68aNWpUq691KfX9+gAuH/fQAah13377rdq2bVsh5iSpWbNmFZb985//1O23367o6Gh17txZY8eO1Xfffedcv2bNGkVGRmr16tUuz3v++ecVGRmprVu3VmmeXl5emjRpktq2basVK1aoqKjIue5/76ErKSnR/Pnz1bNnT0VFRSkuLk5//OMflZubK+nsfW8rVqyQdPaetPJ/pP+7T27p0qV66aWX1KNHD0VFRenAgQPnvYeuXGFhoYYOHaqYmBglJiZq/vz5cjgczvU7duxQZGSkduzY4fK8/93mxeZWvux/76Hbs2eP7rvvPt14442KjY3Vn/70J3366acuY9auXavIyEh9/PHHmjlzprp06aKYmBg99NBDOn78eOX+TwBQJZyhA1DrWrVqpZ07d2rfvn2KiIi46NiFCxfq2WefVUpKiu68804dP35cy5cv1z333KM333xTFotFd9xxhzZv3qxZs2YpISFBv/nNb7R3717Nnz9fd955p2655ZYqz9XLy0u9evXSs88+q48//li///3vzztu/vz5WrRokdLS0hQdHa2TJ09q9+7d+uKLL5SQkKC7775bx44dU25urp566qnzbmPt2rX65ZdfdNddd8nX11f+/v6y2+3nHVtWVqb77rtPHTt21COPPKJt27YpMzNTZWVlGjNmzGXtY2Xmdq6vv/5a99xzj5o2bar77rtP3t7eev311zVo0CAtX75cHTt2dBk/ffp0WSwWjRw5UocPH9bLL7+sadOmae7cuZc1TwCVR9ABqHX33nuvhg0bpn79+ik6Olo33XST4uPjFRcX53Kf2uHDh5WZman09HSNGDHCubxnz576wx/+oFdffdW5/PHHH1fv3r3117/+Vc8//7wmTJigoKAgPfbYY9Web3l0fvvttxcc8/777+uWW27R448/ft71sbGxatOmjXJzcytc2i135MgRbd68WYGBgc5lhw4dOu/YX375RTfffLMmTZokSRowYIBGjBihrKwsDRo0yGUbl1KZuZ1r7ty5Kikp0WuvvaaQkBBJUr9+/XTrrbfq6aef1vLly13GBwQE6IUXXnDec2i32/XKK6+oqKhIfn5+lZ4ngMrjkiuAWpeQkKCVK1eqW7du+uqrr7RkyRINHTpUSUlJevfdd53jNm/eLLvdrpSUFB0/ftz5z69//Wtde+21LpcSg4KCNGXKFOXm5uqee+7Rl19+qRkzZuiqq66q9nybNGkiSTp16tQFx1gsFn399dc6ePBglV+nZ8+elxVi99xzj/PPHh4euueee1RSUqK8vLwqz+FSysrKlJubqx49ejhjTpKaN2+u3r176+OPP9bJkyddnnPXXXe5fICkU6dOKisr0+HDh2ttnsCVjjN0AOpEdHS05s+fr+LiYn311Vd655139NJLL2nMmDF688031bZtWx08eFAOh0M9e/Y87zb+95OfvXr10rp16/T+++/r7rvvVnx8fI3M9fTp05Kkpk2bXnDM6NGj9eCDDyo5OVkRERFKTExU3759df3111f6dYKDgys91tPT0yWoJCk0NFSSajWUjh8/rjNnzjhf61zh4eGy2+367rvvdN111zmXt2zZ0mVc+b2TNput1uYJXOkIOgB1ytfXV9HR0YqOjlabNm302GOPaePGjRo5cqTsdrs8PDyUlZV13q/NKD9zVu6nn37S7t27JUn79++X3W6Xp2f1Lzzs27dPknTttddecMxvf/tbbd68We+++65yc3O1evVqvfzyy5o6darS0tIq9Tq/+tWvqj3Xc13oa1UudF9ebbnQ/wfnfoADQM0i6ADUmw4dOkiSjh07Jklq3bq1HA6HgoODz3tG6H9NmzZNp06d0sMPP6zZs2fr5Zdf1pAhQ6o1p7KyMq1fv16NGzfWTTfddNGxAQEBuuOOO3THHXfo1KlTGjhwoDIzM51Bd7nfW3cxdrtdhYWFLv9eCgoKJJ390In0f2fCzv10rnT+M3iVnVtgYKAaN27sfK1z5efny9PTU7/5zW8qtxMAag330AGodf/+97/Pe3am/OtFwsLCJJ29p8zLy6vC13FIZ8/u/PTTT87HGzduVHZ2th5++GENHz5cvXr10ty5c88bHpVVVlam6dOn68CBAxo0aNBF78c7dy7S2cuzrVu3VnFxsXNZ48aNJdXcpcbyrxqRzv77WLFihXx8fJyXmlu1aiUvLy/95z//cXnea6+9VmFblZ2bl5eXEhIS9O6777p8YOOHH37Q+vXrddNNN9XIfYsAqoczdABq3fTp03XmzBn9v//3/xQWFqaSkhJ98skneuutt9SqVSvdfvvtks6eoUtPT9fs2bN1+PBh9ejRQ02bNtWhQ4f0zjvv6K677tLQoUP1448/KiMjQ3FxcRo4cKAkafLkydqxY4cee+wxvfrqq5e89FpUVKR//vOfkqSff/7Z+UsR3377rXr16nXJrwLp1auXOnfurPbt2ysgIECff/653n77bed8JKl9+/bO/U9MTHR+JUpVNGrUSNu2bdP48eMVHR2tbdu26f3339eIESOcH6zw8/PTrbfequXLl8vDw0MhISF6//33z/vlzZczt/T0dH3wwQcaMGCABgwYIC8vL73++usqLi52+fJlAPWHoANQ6x599FFt3LhRW7du1euvv66SkhK1bNlSAwYM0AMPPODyhcPDhw9XmzZt9NJLL2nBggWSzv5MV0JCgrp16yZJysjIUHFxsWbOnOm8dHj11Vdr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/a5du/TYY49VdfMAAACopCoHncPhuOj606dPy8vLq6qbBwAAQCVd1hcLf/XVV/rqq6+cjz/66COVlZVVGGez2bRy5UqFhoZWf4YAAAC4qMsKunfeeUfz58+XJHl4eOj111/X66+/ft6xFotFTz75ZPVnCAAAgIu6rKC766679Pvf/14Oh0NpaWkaPXq0kpKSXMZ4eHiocePGat26Nb+bCgAAUAcuq7iaN2+u5s2bS5KWLVum8PBwNWvWrFYmBgAAgMqp8im0zp071+Q8AAAAUEXVuia6bds2rV69WoWFhbLZbBU++erh4aF33nmnWhMEAADAxVU56JYsWaLZs2erWbNmio6OVmRkZE3OCwAAAJVU5aBbtmyZunTposWLF8vHx6cm5wQAAIDLUOUvFrbZbEpOTibmAAAA6lmVgy4qKkoFBQU1ORcAAABUQZWDLiMjQ5s3b9a//vWvmpwPAAAALlOV76FLT09XaWmpHn30UWVkZOiaa66Rp6drH3p4eGjdunXVniQAAAAurMpBFxAQoICAAF177bU1OR8AAABcpioH3SuvvFKT8wAAAEAVVfkeOgAAALiHKp+h+89//lOpcb/97W+r+hIAAACohCoH3aBBg+Th4XHJcV9++WVVXwIAAACVUK1fivhfZWVlOnz4sN544w3Z7XY9/PDD1ZocAAAALq3KQde5c+cLrrv99ts1YMAAffjhh4qPj6/qSwAAAKASauVDEZ6enurVq5dWrVpVG5sHAADAOWrtU65Wq1VFRUW1tXkAAAD8/6p8yfW///3veZfbbDZ99NFHWrp0qTp16lTliQEAAKByqhx03bp1u+CnXB0Oh2JiYjR16tQqTwwAAACVU+WgmzFjRoWg8/DwkMViUevWrdW2bdtqTw4AAACXVuWgu/3222tyHgAAAKiiKgfdufbv36/Dhw9Lklq1asXZOQAAgDpUraB75513NGvWLGfMlQsODtaECRPUvXv3ak0OAAAAl1bloNu6datGjx6tli1bauzYsQoPD5ckHThwQG+88YZGjRql559/XklJSTU2WQAAAFRU5aB77rnnFBkZqRUrVqhJkybO5d27d9fAgQM1YMAALViwgKADAACoZVX+YuG9e/eqX79+LjFXrkmTJvrDH/6gvXv3VmtyAAAAuLQqB12jRo1ktVovuN5qtapRo0ZV3TwAAAAqqcpBFxcX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fFj9+vXTkCFDtGjRIo0aNUpbtmxR06ZNJUmHDh1Sv3791Lp1axUXF2vDhg265557tG7dOoWGhp53rsXFxZWeFwD38P3332vWrFl64IEH5O3trenTp2vcuHFq3LixOnXqpLvuuktvvPGGHnnkEXXs2FGtWrXSoUOH1LVrV917773y9PRUTk6Ohg8frpdffllxcXEXfK0xY8bok08+0UMPPaTw8HBt3bpVjzzyiCwWi2655ZY63Gu4HQdwBdi8ebMjIiLCUVhY6HA4HI7Vq1c7brjhBsfXX3/tMi4tLc0xevRo5+OBAwc6YmJiHD/++KNz2axZsxwRERGOV1991bls7969joiICMfmzZvP+/plZWWOkpISR3JysmP27NnO5fPmzXPExMQ4H1d2XgDcw/jx4x2RkZGOffv2OZe98sorjoiICMfTTz/tXGa1Wh3t2rVzvPTSSxW2UX58uPfeex1/+ctfnMvXrFnjiIiIcB5/8vLyHBEREY5t27a5PD89Pd1xxx131PSuwTCcocMVKTc3VxEREWrTpo1KS0udy3/3u99p3bp1LmOvv/56BQYGOh+3adPGOfZ/lx05csS57MCBA/r73/+unTt36scff3QuP3jwYI3MC4B7aN68ua677jrn4/MdIywWiwIDA53HiCNHjmjOnDn64IMP9P3338vhcEiS2rdvf8HXyc3NVUBAgLp06VLh+JCRkaGysjJ5eXnV5K7BIAQdrkg//fST9uzZc96D5/8eEC0Wi8tjHx8fSZKfn59zma+vryTpl19+kSSdPHlS9957rwIDAzVhwgS1bNlSjRo10qRJk5xjqjsvAO6hMscI6exx4pdffpHdbtcDDzygoqIijR49Wtdee60aN26sefPm6bvvvrvg6/z00086ceLEBaPv+++/1zXXXFPNvYGpCDpckfz9/RUZGaknnniiVrb/6aef6siRI1q0aJGuv/565/KioqKLHnBre14A6t8333yjPXv2aMGCBerRo4dz+c8//3zR5/n7+yswMFCLFy8+7/pzryTgykPQ4Yr0u9/9Tlu3blXz5s3VokWLGt9++YG5/L/UJemTTz7R4cOHXS7N1PW8ANS/8rP05x4fDh8+rJ07dzov157P7373Oy1ZskQ+Pj4u/6EISAQdrlD9+vXTypUrNXjwYN17771q06aNioqKtGfPHpWUlOjhhx+u1vZjYmLUpEkTTZ06VcOHD9fRo0eVmZl5yUir7XkBqH9hYWG65pprNHv2bNntdp0+fVrz5s1T8+bNL/q8hIQEde3aVffdd5/uu+8+RUZG6syZM9q/f7+++eYbzuxf4Qg6XJF8fX21bNkyZWZm6vnnn9f333+vgIAA3XDDDRowYEC1t//rX/9azz77rJ566ik9+OCDatOmjaZOnaolS5bU67wA1D9fX19lZmZq2rRpGjNmjH7zm9/ogQce0L///W/t3r37os+dN2+eFi9erNdee02HDx+Wn5+frrvuOt1+++11NHu4Kw9H+UdrAAAAYCR+KQIAAMBwBB0AAIDhCDoAAADDEXQAAACGI+gAAAAMR9ABAAAYjqADAAAwHEEHAABgOIIOAADAcAQdAACA4Qg6AAAAwxF0AFAFJ0+e1BNPPKFu3bqpQ4cOio+P15AhQ/TFF184x3z22WcaOnSobrrpJnXs2FEDBw7Uxx9/7Fx/4MABRUdH69FHH3XZ9kcffaR27drp6aefrrP9AWA2D4fD4ajvSQCAaR5++GG9/fbbGjhwoMLDw3XixAl9/PHHSk1NVZ8+fZSXl6dhw4apQ4cOSk5OloeHh9auXav8/Hy9+uqrio6OliQtXbpUTz31lJ577jl1795dp0+fVt++feXr66t//OMf8vX1rec9BWACgg4AqqBTp07q06ePpkyZUmGdw+HQrbfequDgYC1ZskQeHh6SpJ9//lm9evXStddeqxdeeEGSZLfbNXDgQH3zzTdav369MjMz9frrr2vlypWKioqq030CYC4uuQJAFVgsFn322Wc6evRohXVffvmlDh48qNtuu00//fSTjh8/ruPHj+v06dOKj4/Xf/7zH9ntdkmSp6enZs2apdOnT2vYsGF69dVXNXz4cGIOwGXhDB0AVEF2drYmTJigkpIStW/fXrfccov69eunkJAQZWdna+zYsRd9/ocffih/f3/n4/JLrxEREVq7dq18fHxqexcANCDe9T0BADBRamqqOnXqpM2bNys3N1dLly5VVlaWMjMzVf7fyY8++qjatWt33uc3adLE5XFubq4k6dixYzpx4oSCgoJqdwcANCicoQOAGvDjjz/qD3/4g1q1aqXHHntMaWlpmjZtmu6+++5LPve1115TRkaGxo4dq0WLFqlLly5auHBhHcwaQEPBPXQAcJnKyspUVFTksqxZs2Zq3ry5iouL1aFDB7Vu3VovvPCCTp06VeH5x48fd/65sLBQTz31lJKTkzVixAiNHz9e7733nt58883a3g0ADQhn6ADgMtlsNt1yyy1KTk7W9ddfryZNmuiDDz7QW2+9pQkTJmjIkCHasWOHhg0bpmbNmun2229XixYtdPToUe3YsUNXXXWVnn/+eTkcDg0ePFj79+/Xhg0bFBgYKEm699579fnnn2v9+vVq0aJFPe8tABMQdABwmYqLizV37lzl5uaqsLBQDodDrVu31t13360BAwY4x3355Zd67rnn9OGHH+r06dMKCgpSdHS07r77bsXHx2vZsmV64oknlJmZqZ49ezqf991336l379666aabtHjx4vrYRQCGIegAAAAMxz10AAAAhiPoAAAADEfQAQAAGI6gAwAAMBxBBwAAYDiCDgAAwHAEHQAAgOEIOgAAAMMRdAAAAIYj6AAAAAxH0AEAABiOoAMAADAcQQcAAGC4/w+xmcYDIHqBAgAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "insurance_dataset['sex'].value_counts()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 178
        },
        "id": "ifzpn6YJCrn5",
        "outputId": "efeea1f7-3987-4053-ed15-8845bd935565"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "sex\n",
              "male      676\n",
              "female    662\n",
              "Name: count, dtype: int64"
            ],
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>count</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>sex</th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>male</th>\n",
              "      <td>676</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>female</th>\n",
              "      <td>662</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div><br><label><b>dtype:</b> int64</label>"
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# bmi Distribution\n",
        "plt.figure(figsize=(6,6))\n",
        "sns.distplot(insurance_dataset['bmi'])\n",
        "plt.title('bmi distribution')\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "fN_NYm-uU9eJ",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 764
        },
        "outputId": "a5ccc07c-716e-463f-8a7e-66f267e5ac23"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-11-a971c9a2c426>:3: UserWarning: \n",
            "\n",
            "`distplot` is a deprecated function and will be removed in seaborn v0.14.0.\n",
            "\n",
            "Please adapt your code to use either `displot` (a figure-level function with\n",
            "similar flexibility) or `histplot` (an axes-level function for histograms).\n",
            "\n",
            "For a guide to updating your code to use the new functions, please see\n",
            "https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751\n",
            "\n",
            "  sns.distplot(insurance_dataset['bmi'])\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 600x600 with 1 Axes>"
            ],
            "image/png": "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qsZkZQBOnjyJhx9+GPPmzcPYsWNx/fXXd3veq6++imuuuQYTJkzADTfcgPfffz/EkYa/7du348c//jGKioowefJkzJs3D6+99hrOLRPEex08H374IW699VZccsklGD9+PK6++mo8+eSTXTYbfe+993DDDTdgwoQJuOaaa/D6668rFHFkaWtrQ1FREQoLC/Hll18GPMfP+cD99a9/RWFhYZfHb3/724DzeK/VIdp3nR6Q48eP48MPP8SkSZMgSVKXfzgB4O9//zt++ctf4q677sIll1yCbdu24e6778amTZswefLk0Acdpl588UVkZ2fjwQcfRFJSEvbs2YNf/vKXqK2txd133w2A9zrYWlpaMHHiRCxcuBCJiYk4fvw4Vq5ciePHj2P9+vUAgM8++wx333035s+fj4ceegiffPIJ/vu//xtxcXGYO3euwu8gvP3xj3+E1+vtcpyf8+D605/+hPj4eP/P6enp/v/mvVYRmS6Y1+v1//d//dd/ydddd12Xc7797W/L999/f8Cxm2++Wb7jjjsGPb5I0tjY2OXY//zP/8hTp071///Aez34Xn75ZXnUqFFybW2tLMuyvGTJEvnmm28OOOf++++Xi4uLlQgvYpw4cUKePHmyvGXLFnnUqFHywYMH/c/xcx4cr7/+ujxq1Khuv1s68V6rB4eBBkAUe799lZWVqKioQHFxccDxa6+9Fh9//DFcLtdghhdRkpOTuxwbM2YMbDYb2tvbea9DJDExEYBvU1CXy4W9e/d26UG59tprUVpaiqqqKgUijAxPPPEEFixYgOHDhwcc5+c8dHiv1YXJyiAqKysDgC5fOAUFBXC73aisrFQirIjx+eefIz09HSaTifd6EHm9XjidThw6dAh/+MMfcNVVVyEnJwenTp2C2+1Gfn5+wPkFBQUAvvn80/nZsWMHjh07hmXLlnV5jp/z4Lv++usxZswYXH311Vi9erV/6I33Wl04Z2UQWSwWAIDZbA443vlz5/N0/j777DNs27YN//Vf/wWA93owXXnllairqwMAzJ49G08//TQA3vPBYLfb8dRTT2H58uXd7gTPex48aWlpuOeeezBp0iQIgoD33nsPzzzzDOrq6vDwww/zXqsMkxUKO7W1tVi+fDlmzJiB2267TelwIt6aNWtgt9tx4sQJPP/887jrrrvw5z//WemwItLzzz+PlJQU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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Normal BMI Range --> 18.5 to 24.9**"
      ],
      "metadata": {
        "id": "gB0ZlBnXXT0q"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# cheildren column\n",
        "plt.figure(figsize=(6,6))\n",
        "sns.countplot(x='children',data=insurance_dataset)\n",
        "plt.title('Children')\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 573
        },
        "id": "iNoii-6jXd8X",
        "outputId": "7088a388-8455-46b6-adaf-e3d705fee224"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 600x600 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAiYAAAIsCAYAAADGVWIgAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAAA2eUlEQVR4nO3de3RU5b3/8c9MQhCBSYAFsRKQJEjkEklcHgJNSA+XShOiaVUo0gZrFVC55tRzwJSrUlAPlCC3SsALoBVErLbGFERKhFJ69KAWRbkkCKQniRYyk4TQJDPz+4OV+TlNkGQyZJ6Q92stV53Zz+x8Zy8k7+7ZM2Nxu91uAQAAGMAa6AEAAADqECYAAMAYhAkAADAGYQIAAIxBmAAAAGMQJgAAwBiECQAAMAZhAgAAjEGYAAAAYxAmAAIiJiZGTzzxxBXX7dy5UzExMTp79qznvoyMDGVkZFzxsYcOHVJMTIwOHTrUrFkBtJzgQA8A4Npz+vRpbdy4UQcOHFBpaanatWunfv36KSUlRT/+8Y913XXXBXpEAIYiTAD41Z/+9CfNmjVLISEhSk9PV79+/VRTU6MPP/xQ//3f/60TJ07oySefbPT+0tPTNXbsWIWEhFzFqQGYgjAB4DdnzpxRZmambrzxRr300kvq0aOHZ9tPfvITffnll/rTn/7UpH0GBQUpKCjIz5N6q6qqUocOHa7qzwDQOFxjAsBvNm7cqAsXLuhXv/qVV5TUuemmm3T//fd73ffuu+8qLS1NgwYN0tixY5Wfn++1vaFrTBpSXFysRx99VHFxcRo2bJiWLl2q6urqeusyMjKUlpamI0eO6Cc/+YkGDx6sX//615Kk6upqPfvss/r+97+vQYMG6Xvf+56eeeaZevupuz7mSrMDaDrOmADwm71796pXr1667bbbGrX+ww8/1K5duzRx4kR17NhRW7Zs0cyZM7V371516dKl0T/34sWLuv/++/V///d/ysjIUI8ePfTmm2/qL3/5S4Pry8rKNHnyZI0dO1Z33XWXunXrJpfLpUceeUQffvihxo8fr+joaB07dkwvvfSSTp06pXXr1l2V2QF4I0wA+EVFRYVKSko0atSoRj/m5MmTys3NVe/evSVJCQkJSk9P19tvv62f/vSnjd7Ptm3bdOrUKWVnZyslJUWSNH78eKWnpze4/quvvtLixYs1YcIEz31vvvmm/vznP2vLli26/fbbPffffPPNWrhwof73f//XK7j8NTsAb7yUA8AvKioqJEkdO3Zs9GO++93ven6xS9Itt9yiTp066cyZM0362fn5+erevbt+8IMfeO7r0KGDxo8f3+D6kJAQ3X333V735eXlKTo6WlFRUTp37pznn6FDh0pSvbcc+2t2AN44YwLALzp16iRJqqysbPRjvvOd79S7LzQ0VA6Ho0k/u6ioSDfddJMsFovX/ZGRkQ2uDw8Pr/cuny+//FInT57UsGHDGnzMP/7xD6/b/podgDfCBIBfdOrUST169NDx48cb/ZjLvdvG7Xb7a6wGNfQ5Ki6XS/369dPjjz/e4GNuuOEGr9uBmh241hEmAPxmxIgR2rZtmw4fPqz4+PgW+7k9e/bUsWPH5Ha7vc6aFBYWNnofvXv31ueff65hw4bVO/MCoOVwjQkAv3nooYd0/fXXa968efr666/rbT99+rReeuklv//c5ORklZaWKi8vz3NfVVWVtm/f3uh9pKSkqKSkpMHHXLx4URcuXPDLrAC+HWdMAPhN7969tXz5cmVmZio1NdXzya/V1dU6fPiw8vLy6l106g/jx4/Xyy+/rDlz5ujTTz9V9+7d9eabbzbpo+/T09P1zjvvaOHChTp06JBuu+02OZ1OFRQUKC8vTxs3blRsbKzfZwfgjTAB4FejRo3SW2+9pU2bNmnPnj367W9/q5CQEMXExGju3LmXfadMc3To0EEvvviinnzySW3dulXXXXed7rzzTiUnJ+uhhx5q1D6sVqvWrl2rF198UW+++aZ2796tDh06KCIiQhkZGZe9kBaAf1ncXKkFAAAMwTUmAADAGIQJAAAwBmECAACMYWSYvPHGG/rhD3+o2NhYJSQk6KGHHtLFixc929977z3dddddio2N1ZgxY/T666/X20d1dbWefvppJSYmKi4uTg888IAKCgpa8mkAAIAmMi5M1q9fryeffFKpqanatGmTnnjiCUVERMjpdEqSPvjgA02fPl1xcXHKyclRSkqKfvnLX3p9foEkLVmyRK+99poyMzO1evVqVVdX62c/+5nKy8sD8bQAAEAjGPWunIKCAt15551at26dvve97zW45sEHH1RlZaVeffVVz32/+MUvdPToUeXm5kqSiouLNXLkSC1cuFA//vGPJV36mvMRI0bo0Ucf1eTJk6/+kwEA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6KOPPNsGDBigkJCQwA1nqOnTp2vQoEGKiYnRddddp88//1ybNm1STEyM53N04M1msykhIaHBbQMHDtTAgQNbeKLW4cEHH1RCQoJiYmIkSXv27NH27ds1adIkde/ePcDTNZ3FzcdetmonT57Uk08+qcOHD6tjx45KT09XZmYmvyi+xdmzZzVq1KgGt23evPmyfzG2ZSNHjlRRUVGD2/bs2cMZgAZs2LBBubm5On36tNxut3r27Knvf//7evDBB3m3SRMcOnRIkyZN0o4dOzhjchlLlizR+++/r+LiYrlcLvXp00fjxo1TRkaGLBZLoMdrMsIEAAAYg0vqAQCAMQgTAABgDMIEAAAYgzABAADGIEwAAIAxCBMAAGAMwgQAABiDMAHQonbu3KmYmBj97W9/u+LajIwMZWRkeG6fPXtWMTEx2rlz5xUfO3fuXI0cObJZswJoeYQJAAAwBt+VA8BYmzZtCvQIAFoYYQLAWFf7O59qa2vlcrn4binAILyUA8DvSkpKlJWVpaSkJA0aNEgjR47UwoULVV1d7VlTXV2tZcuWaejQoYqLi9O0adN07tw5r/386zUml/Puu+8qLS1NsbGxSktL0+7du+utqbs+ZdOmTXrxxRc1evRoxcbG6uTJk5IufSHmzJkzNWTIEMXGxuruu+/Wnj17vPZRd33Mhx9+eMXZAfiGMyYA/KqkpET33nuvysvLNX78eEVFRamkpER//OMfdfHiRc+6JUuWyGazafr06SoqKtJLL72kJ554QtnZ2U36efv379eMGTPUt29f/eIXv9D58+f1+OOP64Ybbmhw/c6dO/XPf/5T48ePV0hIiEJDQ3X8+HHdd999Cg8P1+TJk3X99dfrnXfe0bRp07R69Wp9//vf99qHv2YHUB9hAsCvfv3rX+vrr7/W9u3bvb6mftasWfrml5mHhYXp+eef93wtu8vl0pYtW1ReXq7OnTs3+uctX75c3bp10yuvvOJ53JAhQ/Tzn/9cPXv2rLe+uLhYu3fvVteuXT33/exnP9N3vvMdvf76656XdSZOnKj77rtPy5cvrxcm/podQH28lAPAb1wul959912NGDHCK0rq1P0il6Tx48d73b799tvldDpVVFTU6J9XWlqqo0eP6kc/+pFXECQmJqpv374NPuaOO+7wipKysjL95S9/UUpKiioqKnTu3DmdO3dO58+fV1JSkk6dOqWSkhKvffhjdgAN44wJAL85d+6cKioqdPPNN19x7Y033uh122azSZIcDkejf97f//53SdJNN91Ub1tkZKQ+++yzevdHRER43T59+rTcbrdWrVqlVatWNfhz/vGPfyg8PNyvswNoGGECICCs1oZP2H7z5Z6r4brrrvO67XK5JEk///nPNXz48AYf07t3b6/bgZodaAsIEwB+07VrV3Xq1EnHjx9vkZ9Xd+biyy+/rLetsLCwUfvo1auXJKldu3b67ne/67/hAPiEa0wA+I3VatXo0aO1d+/eBj9y3t9nFHr06KH+/fvrjTfeUHl5uef+AwcO6MSJE43aR7du3TRkyBBt27ZNpaWl9bbzNmCgZXHGBIBf/cd//IcOHDigjIwMjR8/XtHR0frqq6+Ul5enV1555ar8vKlTp2rixIm65557VFZWpq1bt+rmm2/WhQsXGrWPhQsXauLEibrzzjs1fvx49erVS19//bU++ugjFRcX66233vL73AAaRpgA8Kvw8HBt375dq1at0u9//3tVVFQoPDxcycnJ9a7v8Ifk5GStWrVK2dnZWrFihXr37q1ly5Zpz549+utf/9qoffTt21evv/661qxZozfeeENlZWXq2rWrBgwYoGnTpvl9ZgCXZ3FztRYAADAE15gAAABjECYAAMAYhAkAADAGYQIAAIxBmAAAAGMQJgAAwBiECQAAMAZhAgAAjEGYAAAAYxAmAADAGIQJAAAwBmECAACMQZgAAABj/D+LfVe7MPeEJAAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "insurance_dataset['children'].value_counts()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 304
        },
        "id": "Vtv7t-SIY8Z1",
        "outputId": "b54c93f7-c871-4e55-a43f-0f1039b01524"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "children\n",
              "0    574\n",
              "1    324\n",
              "2    240\n",
              "3    157\n",
              "4     25\n",
              "5     18\n",
              "Name: count, dtype: int64"
            ],
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>count</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>children</th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>574</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>324</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>240</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>157</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>25</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>18</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div><br><label><b>dtype:</b> int64</label>"
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(6,6))\n",
        "sns.countplot(x='smoker',data=insurance_dataset)\n",
        "plt.title('Smoker')\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 573
        },
        "id": "1Tpn9ALJZRsJ",
        "outputId": "3d484a29-b641-4237-8cd8-ee441e337d5b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 600x600 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAjAAAAIsCAYAAADs5ZOPAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAAA02UlEQVR4nO3deVxU9eL/8fcMiwsyCH5dckvAIFMIyityJTTXADPzarlbptnigmmp3DI1r1pX01S0RO/ta1qa2rdNJM26YWZ23TIzsytYaKmVOoNLss3vDx/Or7lo6QCOn3g9H48eNed8zpnPQQZfnXNmsDidTqcAAAAMYvX2BAAAAK4UAQMAAIxDwAAAAOMQMAAAwDgEDAAAMA4BAwAAjEPAAAAA4xAwAADAOAQMAAAwDgEDAJLGjx+v2NhYb08DwGXy9fYEAFReX3/9tdLT0/XFF1/op59+Us2aNdW0aVO1b99eAwYM8Pb0AFzDCBgAXrFjxw4NHDhQ9evXV69evVS7dm398MMP+vzzz7V06VICBsBvImAAeMWLL76owMBArV69WjabzW3dzz//7KVZVZxz587Jz89PVitX7oHywCsJgFd89913atq0aal4kaRatWq5/jsyMlJTpkzRunXrlJycrOjoaN177736+uuvJUkrVqxQp06dFBUVpQEDBujQoUOl9rdu3Tr16NFD0dHRiouL09ixY3X06NHfneNXX32l1q1ba8CAATp9+rQk6ejRo5owYYL+/Oc/q0WLFkpJSdHq1avdttu6dasiIyO1du1azZ49W7fddptuvvlmnTp16oq+RgAujTMwALyiQYMG2rlzp/bv36+IiIjfHLtt2zZ98MEH6tu3ryRp0aJFeuihhzRkyBC9+uqr6tu3r+x2uxYvXqy0tDQtXbrUte0bb7yhCRMmKCoqSo899ph+/vlnLV26VDt27NCbb7550YCSpN27d2vIkCFq0aKFFixYoKpVq+qnn37SPffcI4vFon79+ikkJETZ2dn661//qlOnTum+++5z28eCBQvk5+enBx54QAUFBfLz8yvbFw2ACwEDwCsGDx6soUOHqnv37oqOjtatt96q+Ph4xcXFlfqLPjc3V+vWrVPDhg0lSUFBQZo4caIWLlyorKws1ahRQ5JUUlKil156SYcOHVLDhg1VWFiomTNnKiIiQsuXL1eVKlUkSbfeequGDRuml19+WSNHjiw1t+3bt+vBBx9Uy5YtNW/ePPn7+0uSZs+ereLiYr3zzjsKDg6WJPXp00ePPfaY5s+fr969e6tq1aqu/Zw7d05r1qxxWwagfHAJCYBXtGnTRitWrFD79u21b98+LV68WA888IASExO1ceNGt7Hx8fGueJGkm2++WZLUuXNnV7xIUnR0tCQpLy9PkrRnzx79/PPP6tOnjyteJKldu3YKCwvTv/71r1Lz+vTTTzVkyBDFx8e7xYvT6dT69evVvn17OZ1OHT9+3PVPQkKC8vPz9eWXX7rtq3v37sQLUEE4AwPAa6KjozV//nwVFBRo3759ev/99/Xyyy9r1KhRevPNN9W0aVNJ0nXXXee23YVoqVevntvywMBASZLD4ZAkff/995Kk0NDQUs8dFham7du3uy07d+6chg0bpubNm2vOnDny9f3/PyKPHz8uh8OhlStXauXKlRc9nuPHj7s9/nV0AShfBAwAr/P391d0dLSio6PVpEkTTZgwQVlZWRo+fLgkycfH56LbXWq50+n0eB6JiYn64IMPtGnTJt1+++2udSUlJZKkbt266e67777o9pGRkW6POfsCVBwCBsA1pUWLFpKkY8eOlXlf9evXl3T+Hpr4+Hi3dbm5ua71F1gsFs2cOVOPPPKIRo0apYyMDMXFxUmSQkJCFBAQoJKSEv35z38u89wAlA33wADwik8//fSiZ0o++ugjSecv8ZRVixYtVKtWLa1YsUIFBQVuz3HgwAG1a9eu1Db+/v6aP3++oqKi9NBDD2n37t2Szp/t6dKli9577z3t37+/1Hb/ffkIQMXiDAwAr5g6darOnj2rTp06KSwsTIWFhdqxY4fWrVunBg0aqEePHmV+Dj8/P40dO1YTJkxQ//79lZKS4nobdYMGDUq97fmCqlWr6qWXXtLAgQM1dOhQvfLKK4qIiNCYMWO0detW3XPPPerVq5eaNm0qu92uL7/8Ulu2bNFnn31W5jkDuDwEDACveOKJJ5SVlaWPPvpIK1euVGFhoerXr6++ffvq4YcfvuTns1ypHj16qGrVqsrIyNDMmTNVvXp1dezYUY8//vhvPkeNGjW0ZMkS9e/fX4MHD9by5ct1/fXXa9WqVUpPT9eGDRv02muvuX5/09ixY8tlvgAuj8Xp6d1uAAAAXsI9MAAAwDgEDAAAMA4BAwAAjEPAAAAA4xAwAADAOAQMAAAwDgEDAACMwwfZVQCn06mSEj5eBwCAK2G1WmSxWC5rLAFTAUpKnDp+/LS3pwEAgFFCQgLk43N5AcMlJAAAYBwCBgAAGIeAAQAAxiFgAACAcQgYAABgHAIGAAAYh4ABAADGIWAAAIBxCBgAAGAcAgYAABiHgAEAAMYhYAAAgHEIGAAAYBwCBgAAGIeAAQAAxiFgAACAcQgYAABgHAIGAAAYh4ABAADG8fX2BADgj8RqtchqtXh7GkCFKilxqqTE6dU5EDAAUE6sVotq1qwuHx9ObuOPrbi4RCdPnvFqxBAwAFBOrFaLfHysSn9tsw4fs3t7OkCFaFAnSI/2aSOr1ULAAMAfyeFjdh08fMLb0wD+0DjPCQAAjEPAAAAA4xAwAADAOAQMAAAwDgEDAACMQ8AAAADjEDAAAMA4BAwAADAOAQMAAIxDwAAAAOMQMAAAwDgEDAAAMA4BAwAAjEPAAAAA4xAwAADAOAQMAAAwDgEDAACMQ8AAAADjXFMB8+2332rixIm66667dNNNN6lr164XHbdq1Sp16dJFUVFR6tatmz788MNSY/Lz85WWlqZWrVopNjZWI0eO1LFjx0qN27Fjh+69915FR0fr9ttv16JFi+R0Osv92AAAQPm5pgLmm2++0UcffaTrr79e4eHhFx2zdu1aPfXUU0pKSlJGRoZiYmI0fPhw7dq1y21camqqNm/erEmTJmnmzJnKzc3V0KFDVVRU5Brz7bff6oEHHlDt2rX10ksvadCgQZo7d67+8Y9/VORhAgCAMvL19gR+rX379urYsaMkafz48dqzZ0+pMXPnzlVKSopSU1MlSa1bt9b+/fuVnp6ujIwMSdLOnTv18ccfa8mSJUpISJAkhYaGKjk5WevXr1dycrIkacmSJQoODtbzzz8vf39/xcfH6/jx43rxxRc1YMAA+fv7X4WjBgAAV+qaOgNjtf72dPLy8nTw4EElJSW5LU9OTtaWLVtUUFAgScrOzpbNZlObNm1cY8LCwtSsWTNlZ2e7lmVnZ6tDhw5uoZKcnCyHw6GdO3eWxyEBAIAKcE0FzO/JycmRdP5syq+Fh4ersLBQeXl5rnGhoaGyWCxu48LCwlz7OHPmjH744QeFhYWVGmOxWFzjAADAteeauoT0e+x2uyTJZrO5Lb/w+MJ6h8OhwMDAUtsHBQW5Lkvl5+dfdF/+/v6qVq2aa1+e8vU1qg0BlAMfH173qDy8/f1uVMCYwmq1KDg4wNvTAACgwths1bz6/EYFTFBQkKTzZ09q167tWu5wONzW22w2HTlypNT2drvdNebCGZoLZ2IuKCgo0NmzZ13jPFFS4pTDccbj7QGYycfH6vUf6sDV4nCcVXFxSbnu02ardtlndowKmAv3q+Tk5Ljdu5KTkyM/Pz81atTINW7Lli1yOp1u98Hk5uYqIiJCklS9enVdd911pe51yc3NldPpLHVvzJUqKirfP1QAAK4lxcUlXv27zqgLto0aNVKTJk2UlZXltjwzM1Px8fGudxMlJibKbrdry5YtrjG5ubnau3evEhMTXcsSExO1ceNGFRYWuu3LZrMpNja2go8GAAB46po6A3P27Fl99NFHkqTDhw/r1KlTrlhp1aqVQkJCNGLECI0dO1aNGzdWXFycMjMztXv3bi1btsy1n9jYWCUkJCgtLU3jxo1TlSpVNHv2bEVGRqpz586ucQ888IDeeecdjRkzRn369NH+/fu1ZMkSjR49ms+AAQDgGmZxXkOfm3/o0CF16NDhouuWLl2quLg4Sed/lUBGRoa+//57hYaG6rHHHtPtt9/uNj4/P1/Tp0/Xhg0bVFRUpISEBD355JOqW7eu27gdO3ZoxowZ+uqrrxQSEqJ+/fpp6NChpd6CfSWKi0t0/Phpj7cHYCZfX6uCgwOU9kKmDh4+4e3pABWiSYNgTRuVrBMnTpf7JaSQkIDLvgfmmgqYPwoCBqicCBhUBtdKwBh1DwwAAIBEwAAAAAMRMAAAwDgEDAAAMA4BAwAAjEPAAAAA4xAwAADAOAQMAAAwDgEDAACMQ8AAAADjEDAAAMA4BAwAADAOAQMAAIxDwAAAAOMQMAAAwDgEDAAAMA4BAwAAjEPAAAAA4xAwAADAOAQMAAAwDgEDAACMQ8AAAADjEDAAAMA4BAwAADAOAQMAAIxDwAAAAOMQMAAAwDgEDAAAMA4BAwAAjEPAAAAA4xAwAADAOAQMAAAwDgEDAACMQ8AAAADjEDAAAMA4BAwAADAOAQMAAIxDwAAAAOMQMAAAwDgEDAAAMA4BAwAAjEPAAAAA4xAwAADAOAQMAAAwDgEDAACMQ8AAAADjEDAAAMA4BAwAADAOAQMAAIxDwAAAAOMQMAAAwDgEDAAAMA4BAwAAjEPAAAAA4xAwAADAOAQMAAAwDgEDAACMQ8AAAADjEDAAAMA4BAwAADAOAQMAAIxDwAAAAOMQMAAAwDgEDAAAMA4BAwAAjEPAAAAA4xAwAADAOAQMAAAwDgEDAACMQ8AAAADjGBkwGzduVK9evRQbG6uEhASNGjVKeXl5pcatWrVKXbp0UVRUlLp166YPP/yw1Jj8/HylpaWpVatWio2N1ciRI3Xs2LGrcRgAAMBDxgXM1q1bNXz4cDVt2lTp6elKS0vTvn37NHjwYP3yyy+ucWvXrtVTTz2lpKQkZWRkKCYmRsOHD9euXbvc9peamqrNmzdr0qRJmjlzpnJzczV06FAVFRVd5SMDAACXy9fbE7hSa9euVf369TVt2jRZLBZJUkhIiAYNGqQ9e/aoZcuWkqS5c+cqJSVFqampkqTWrVtr//79Sk9PV0ZGhiRp586d+vjjj7VkyRIlJCRIkkJDQ5WcnKz169crOTn56h8gAAD4XcadgSkqKlJAQIArXiQpMDBQkuR0OiVJeXl5OnjwoJKSkty2TU5O1pYtW1RQUCBJys7Ols1mU5s2bVxjwsLC1KxZM2VnZ1f0oQAAAA8ZdwamR48eeuutt7R8+XJ169ZNJ0+e1PPPP6+bbrpJt9xyiyQpJydH0vmzKb8WHh6uwsJC5eXlKTw8XDk5OQoNDXWLIel8xFzYh6d8fY1rQwBl5OPD6x6Vh7e/340LmJYtW2r+/PkaM2aMpkyZIklq1qyZFi9eLB8fH0mS3W6XJNlsNrdtLzy+sN7hcLjO3vxaUFCQ9uzZ4/EcrVaLgoMDPN4eAIBrnc1WzavPb1zA7NixQ0888YTuuecetWvXTidPntSCBQv04IMP6tVXX1XVqlW9PUWVlDjlcJzx9jQAXGU+Plav/1AHrhaH46yKi0vKdZ82W7XLPrNjXMBMnTpVrVu31vjx413LYmJi1K5dO7311lu69957FRQUJOn8W6Rr167tGudwOCTJtd5ms+nIkSOlnsNut7vGeKqoqHz/UAEAuJYUF5d49e864y7YHjhwQDfeeKPbsnr16ik4OFjfffedpPP3sEgqdR9LTk6O/Pz81KhRI9e43Nxc182/F+Tm5rr2AQAArj3GBUz9+vW1d+9et2WHDx/WiRMn1KBBA0lSo0aN1KRJE2VlZbmNy8zMVHx8vPz9/SVJiYmJstvt2rJli2tMbm6u9u7dq8TExAo+EgAA4CnjLiH17t1b06ZN09SpU9W+fXudPHlSCxcuVK1atdzeNj1ixAiNHTtWjRs3VlxcnDIzM7V7924tW7bMNebCJ/mmpaVp3LhxqlKlimbPnq3IyEh17tzZG4cHAAAug3EBM3DgQPn7++u1117TmjVrFBAQoJiYGM2ZM0fBwcGucV27dtXZs2eVkZGhRYsWKTQ0VPPnz1dsbKzb/ubMmaPp06dr4sSJKioqUkJCgp588kn5+hr3pQEAoNKwOP/7BhCUWXFxiY4fP+3taQC4ynx9rQoODlDaC5k6ePiEt6cDVIgmDYI1bVSyTpw4Xe438YaEBFz2u5CMuwcGAACAgAEAAMYhYAAAgHEIGAAAYBwCBgAAGIeAAQAAxiFgAACAcQgYAABgHAIGAAAYh4ABAADGIWAAAIBxCBgAAGAcAgYAABiHgAEAAMYhYAAAgHEIGAAAYBwCBgAAGIeAAQAAxiFgAACAcQgYAABgHAIGAAAYh4ABAADGIWAAAIBxCBgAAGAcAgYAABiHgAEAAMYhYAAAgHEIGAAAYBwCBgAAGIeAAQAAxiFgAACAcQgYAABgHAIGAAAYh4ABAADGIWAAAIBxCBgAAGAcAgYAABiHgAEAAMYhYAAAgHEIGAAAYBwCBgAAGIeAAQAAxiFgAACAcQgYAABgHAIGAAAYh4ABAADGIWAAAIBxCBgAAGAcAgYAABiHgAEAAMYhYAAAgHEIGAAAYBwCBgAAGIeAAQAAxiFgAACAcQgYAABgHAIGAAAYh4ABAADGIWAAAIBxCBgAAGAcAgYAABiHgAEAAMYhYAAAgHEIGAAAYBwCBgAAGIeAAQAAxiFgAACAcQgYAABgHAIGAAAYx9iA+b//+z91795dUVFRiouL05AhQ/TLL7+41n/wwQfq1q2boqKi1KVLF61Zs6bUPgoKCvTss8+qTZs2iomJ0f3336+cnJyreRgAAMADRgbMwoUL9cwzzyg5OVlLlizRlClT1LBhQxUXF0uStm3bpuHDhysmJkYZGRlKSkrSX//6V2VlZbntZ+rUqVq1apVGjx6tefPmqaCgQPfdd5/y8/O9cVgAAOAy+Xq64ZtvvqmWLVuqYcOGF11/6NAhbdu2Td27d/f0KS4qJydH8+fP14IFC9S2bVvX8i5durj+e+HChYqOjtaUKVMkSa1bt1ZeXp7mzp2rO+64Q5J05MgRrV69Wk8//bR69uwpSYqKitLtt9+uFStWaOjQoeU6bwAAUH48PgMzYcIE7dy585Lrd+/erQkTJni6+0t644031LBhQ7d4+bWCggJt3brVFSoXJCcn68CBAzp06JAk6eOPP1ZJSYnbuJo1a6pNmzbKzs4u93kDAIDy43HAOJ3O31x/5swZ+fj4eLr7S/r8888VERGhBQsWKD4+Xi1atFDv3r31+eefS5K+++47FRYWKiwszG278PBwSXLd45KTk6NatWopKCio1DjugwEA4Np2RZeQ9u3bp3379rkeb9u2zXXfya85HA6tWLFCoaGhZZ/hf/nxxx+1Z88e7d+/X08//bSqVaumF198UYMHD9b69etlt9slSTabzW27C48vrHc4HAoMDCy1f5vN5hpTFr6+Rt5eBKAMfHx43aPy8Pb3+xUFzPvvv6/58+dLkiwWi1auXKmVK1dedKzNZtOzzz5b9hn+F6fTqTNnzuiFF17QjTfeKEm6+eab1b59ey1btkwJCQnl/pxXymq1KDg4wNvTAACgwths1bz6/FcUMPfcc4/atWsnp9OpXr16aeTIkUpMTHQbY7FYVK1aNTVu3Fi+vh7fI3xJNptNNWvWdMWLdP7elZtuukn/+c9/lJKSIkml3knkcDgkyXXJyGaz6dSpU6X273A4Sl1WulIlJU45HGfKtA8A5vHxsXr9hzpwtTgcZ1VcXFKu+7TZql32mZ0rKow6deqoTp06kqSlS5cqPDxctWrVuvIZlkHTpk313XffXXTduXPn1LhxY/n5+SknJ0e33Xaba92F+1ou3BsTFhamn376SXa73S1YcnJySt0/44miovL9QwUA4FpSXFzi1b/rPL6A1apVq6seL5J0++236+TJk/rqq69cy06cOKEvv/xSzZs3l7+/v+Li4vTee++5bZeZmanw8HDX274TEhJktVq1fv161xi73a6PP/641FklAABwbSnTNZ5NmzZp9erVysvLk8PhKPXOJIvFovfff79ME/xvHTt2VFRUlEaOHKnRo0erSpUqWrRokfz9/dW3b19J0sMPP6yBAwdq0qRJSkpK0tatW/Xuu+9q9uzZrv3Uq1dPPXv21HPPPSer1aq6devqpZdeUmBgoHr37l2ucwYAAOXL44BZvHixZs2apVq1aik6OlqRkZHlOa9LslqtWrRokaZPn66JEyeqsLBQ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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "insurance_dataset['smoker'].value_counts()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 178
        },
        "id": "8HEFBgQEbAQf",
        "outputId": "8b3c5603-a555-42c2-d523-6966b1b4b6db"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "smoker\n",
              "no     1064\n",
              "yes     274\n",
              "Name: count, dtype: int64"
            ],
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>count</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>smoker</th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>no</th>\n",
              "      <td>1064</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>yes</th>\n",
              "      <td>274</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div><br><label><b>dtype:</b> int64</label>"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(6,6))\n",
        "sns.countplot(x='region',data=insurance_dataset)\n",
        "plt.title('region')\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 573
        },
        "id": "O4uhHYCtb4O5",
        "outputId": "21667a89-2473-4dc1-cf21-fbc371c252d9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 600x600 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAiYAAAIsCAYAAADGVWIgAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAABEn0lEQVR4nO3de1xUdR7/8fcAQl4YUPOyiRegnDRRSLwF6nrPS5mlZRes1jRLTCwNctXVckUr00RzU1m7l9e12sgtrTTNNS1bf6WViqayqaUxg4pxO78//DE/Z/GKA/MFX8/Ho0fMOd/5ns85X4Z58z1fRptlWZYAAAAM4OfrAgAAAIoRTAAAgDEIJgAAwBgEEwAAYAyCCQAAMAbBBAAAGINgAgAAjEEwAQAAxiCYAAAAYxBMAFQ6Bw8elMPh0MqVK31dCoBLRDABAADGsPFv5QCobCzLUl5engICAuTv7+/rcgBcAmZMAPjUyZMnvd6nzWZTUFAQoQSogAgmAMpNWlqaHA6Hdu/erSeeeEJt2rTRPffcI0l69913dfvtt6tly5Zq27atxowZo59//rlEH2+++aa6deumli1bauDAgdq6dasSEhKUkJDgbnOuNSabNm3SPffco+joaMXGxuqRRx7Rnj17zlrjTz/9pJSUFMXGxqp169Z66qmnlJubWwZXBcCZCCYAyt3o0aOVm5urMWPGaNCgQZo/f76Sk5PVuHFjpaSkaMiQIdq0aZPuvfdeuVwu9/PeeustPf3006pfv77GjRun2NhYjRw5UocOHbrgMb/44gs99NBDOnr0qBITE/XAAw9o27Ztuvvuu3Xw4MES7ZOSknTixAk9/vjj6t27t1auXKm5c+d69ToAKCnA1wUAuPJcf/31mjlzpiQpKytLPXr0UFJSkkaMGOFu07NnTw0YMEBvvfWWRowYoby8PL344ouKiorSq6++qoCA0z++HA6HUlJSVL9+/fMe89lnn1VISIiWLFmi0NBQSVL37t01YMAApaWlacaMGR7tmzVrpmnTprkfZ2dna/ny5Ro3bpw3LgGAc2DGBEC5Gzx4sPvrjz/+WEVFRerdu7eOHTvm/u/qq69W48aNtXnzZknSt99+q+zsbN15553uUCJJt9xyi0JCQs57vCNHjmjnzp0aMGCAO5RIpwPSTTfdpHXr1p23RkmKjY1Vdna2jh8/XppTBnCRmDEBUO7CwsLcX+/bt0+WZalnz55nbVscQv773/9Kkho1alRif4MGDc57vOLnhoeHl9gXGRmpDRs26OTJk6pWrZp7+zXXXOPRzm63S5KcTqdq1Khx3uMBKD2CCYByFxQU5P66qKhINptNCxcuPOtf0ZwZFsqTn9/ZJ5T5hAWgbBFMAPhUo0aNZFmWwsLCzjqjUax4BmP//v1q3769e3tBQYGysrLkcDgu+Ny9e/eW2JeZmamaNWv6LAAB8MQaEwA+1bNnT/n7+2vu3LklZiMsy9Jvv/0mSWrRooVCQ0O1dOlSFRQUuNu8//77cjqd5z1G3bp11axZM61atcrjr3x+/PFHbdy4UZ07d/biGQG4HMyYAPCpRo0aKSkpSTNnzlRWVpa6d++u6tWr6+DBg1qzZo3uvPNODR06VIGBgRo1apSeeeYZ3X///erdu7eysrK0cuXKEutOzubJJ5/UsGHDdNddd2ngwIE6deqU3njjDQUHBysxMbEczhTAxSCYAPC54cOHq0mTJnrllVc0b948SVL9+vUVFxenrl27utvdd999sixLixcv1owZM3T99ddr/vz5mjp1qse6lbO56aabtGjRIs2ZM0dz5sxRQECA2rRpo3Hjxqlhw4Zlen4ALh7/Vg6ACq2oqEgdOnRQjx49NHXqVF+XA+AyscYEQIXx+++/l1iHsmrVKmVnZ6tt27Y+qgqAN3ErB0CF8c033yg1NVU333yzQkNDtWPHDi1fvlxNmzbVzTff7OvyAHgBwQRAhdGgQQPVr19fr7/+upxOp0JCQtS/f3+NHTtWgYGBvi4PgBewxgQAABiDNSYAAMAYBBMAAGAMggkAADAGi18vkWVZKipiWQ4AAJfCz88mm812wXYEk0tUVGTp2LETvi4DAIAKpVat6vL3v3Aw4VYOAAAwBsEEAAAYg2ACAACMQTABAADGIJgAAABjEEwAAIAxCCYAAMAYBBMAAGAMggkAADAGwQQAABiDYAIAAIxBMAEAAMYgmAAAAGMQTAAAgDEIJgAAwBgEEwAAYAyCCQAAMAbBBAAAGINgAgAAjBHg6wKAisTPzyY/P5uvy7iiFBVZKiqyfF0GgHJCMAEukp+fTaGh1eTvz0RjeSosLFJ29knCCXCFIJgAF8nPzyZ/fz/Ne3ujso44fV3OFaFB3RCNvDtOfn42gglwhSCYAJco64hT+7J+83UZAFApMScNAACMQTABAADGIJgAAABjEEwAAIAxCCYAAMAYBBMAAGAMggkAADAGwQQAABjDqGCybt063XfffWrfvr1atGihbt26KTU1VTk5Oe42KSkpcjgcJf5bv369R195eXmaMWOG4uLiFB0drQcffFCZmZnlfUoAAOASGPXJr9nZ2WrZsqUSEhIUGhqqXbt2KS0tTbt27dLf//53d7uGDRvq+eef93huZGSkx+OpU6cqIyNDKSkpqlevnv72t7/pgQce0AcffKDg4OByOR8AAHBpjAom/fv393jcrl07BQYGauLEiTp8+LDq1asnSbrqqqsUHR19zn4OHTqk5cuX6y9/+YsGDhwoSYqKilKXLl30zjvvaNiwYWV2DgAAoPSMupVzNqGhoZKk/Pz8i37Ohg0bVFRUpJtvvtmjn7i4uBK3fAAAgDmMDCaFhYX6/fff9d1332nevHnq2rWrwsLC3Pt/+ukntW7dWi1atNDtt9+uNWvWeDw/MzNTtWvXVkhIiMf2yMhI1pkAAGAwo27lFOvSpYsOHz4sSerYsaNmzpzp3tesWTNFRUXp2muvVU5Ojt5++22NHDlSL774onuGxOVynXUdid1ul9N5+f9cfUCAkXkOZczfn3H3Fa49cOUwMpgsWLBAubm52r17t+bPn68RI0Zo8eLF8vf31/333+/RtmvXrho8eLDmzJnjceumrPj52VSzZvUyPw6A/89ur+rrEgCUEyODyfXXXy9JiomJUVRUlPr376+PP/74rMHDz89PPXv21HPPPadTp07pqquukt1u1/Hjx0u0dblcJW7vXKqiIksu18nL6gMVk7+/H2+QPuJy5aqwsMjXZQC4DHZ71Yua/TQymJzJ4XCoSpUq2r9//0U/JyIiQr/++qucTqdHEMnMzFRERMRl11RQwA9IoDwVFhbxugOuEMbfuP3Pf/6j/Px8j8WvZyoqKtLq1at13XXX6aqrrpIkxcfHy8/PTx999JG7ndPp1IYNG9SpU6dyqRsAAFw6o2ZMEhMT1aJFCzkcDl111VX6/vvvlZ6eLofDoe7duysrK0spKSnq27evGjduLKfTqbffflvffvut0tLS3P3Ur19fAwcO1LPPPis/Pz/Vq1dPL7/8soKDgzV48GAfniEAADgfo4JJy5YtlZGRoQULFsiyLDVo0ECDBg3S0KFDFRgYqOrVq6tGjRqaP3++jh49qipVqqhFixZauHChOnbs6NHXhAkTVL16dc2cOVMnTpzQjTfeqMWLF/OprwAAGMxmWZbl6yIqksLCIh07dsLXZcAHAgL8VLNmdY1/MUP7sn7zdTlXhCYNamra6D767bcTrDEBKrhatapf1OJX49eYAACAKwfBBAAAGINgAgAAjEEwAQAAxiCYAAAAYxBMAACAMQgmAADAGAQTAABgDIIJAAAwBsEEAAAYg2ACAACMQTABAADGIJgAAABjEEwAAIAxCCYAAMAYBBMAAGAMggkAADAGwQQAABiDYAIAAIxBMAEAAMYgmAAAAGMQTAAAgDECfF1AZebnZ5Ofn83XZVxRioosFRVZvi4DFQSv0fLHaxQXQjApI35+NoWGVpO/P5NS5amwsEjZ2Sf5wYcL4jXqG7xGcSEEkzLi52eTv7+f5r29UVlHnL4u54rQoG6IRt4dJz8/Gz/0cEG8RstfWb9GmQErf2UxA0YwKWNZR5zal/Wbr8sAcA68RisHZsB8oyxmwAgmAIAKjxmw8ldWM2AEEwBApcEMWMXHnBcAADAGwQQAABiDYAIAAIxBMAEAAMYgmAAAAGMQTAAAgDEIJgAAwBgEEwAAYAyCCQAAMAbBBAAAGINgAgAAjEEwAQAAxiCYAAAAYxBMAACAMQgmAADAGAQTAABgDIIJAAAwBsEEAAAYg2ACAACMQTABAADGMCqYrFu3Tvfdd5/at2+vFi1aqFu3bkpNTVVOTo5Hu08++US33nqroqKi1KtXL61YsaJEX3l5eZoxY4bi4uIUHR2tBx98UJmZmeV1KgAAoBSMCibZ2dlq2bKlpkyZovT0dD344INatWqVRo8e7W6zdetWJSYmKjo6WgsXLlTv3r315z//WatXr/boa+rUqVq2bJnGjBmjtLQ05eXl6YEHHigRcgAAgDkCfF3Amfr37+/xuF27dgoMDNTEiRN1+PBh1atXT/Pnz1fLli319NNPS5Lat2+vAwcOaM6cObr55pslSYcOHdLy5cv1l7/8RQMHDpQkRUVFqUuXLnrnnXc0bNiw8j0xAABwUYyaMTmb0NBQSVJ+fr7y8vK0efNmdwAp1qdPH+3Zs0cHDx6UJG3YsEFFRUUe7UJDQxUXF6f169eXW+0AAODSGBlMCgsL9fvvv+u7777TvHnz1LVrV4WFhWn//v3Kz89XRESER/vIyEhJcq8hyczMVO3atRUSElKiHetMAAAwl1G3cop16dJFhw8fliR17NhRM2fOlCQ5nU5Jkt1u92hf/Lh4v8vlUnBwcIl+7Xa7u83lCAi4cJ7z9zcy810RyuraM6a+UxbXnvH0HcazcvH2tTcymCxYsEC5ubnavXu35s+frxEjRmjx4sW+LkuS5OdnU82a1X1dBs7Dbq/q6xLgZYxp5cJ4Vi7eHk8jg8n1118vSYqJiVFUVJT69++vjz/+WNdee60klfjLGpfLJUnuWzd2u13Hjx8v0a/L5Spxe+dSFRVZcrlOXrCdv78fLz4fcblyVVhY5PV+GVPfKYsxZTx9h/GsXC52PO32qhc1u2JkMDmTw+FQlSpVtH//fnXt2lVVqlRRZmamOnbs6G5TvG6keO1JRESEfv31VzmdTo8gkpmZWWJ9SmkUFHj/TQ/eU1hYxBhVMoxp5cJ4Vi7eHk/jb8r95z//UX5+vsLCwhQYGKh27drpX//6l0ebjIwMRUZGKiwsTJIUHx8vPz8/ffTRR+42TqdTGzZsUKdOncq1fgAAcPGMmjFJTExUixYt5HA4dNVVV+n7779Xenq6HA6HunfvLkl65JFHNGTIEE2ePFm9e/fW5s2b9c9//lOzZs1y91O/fn0NHDhQzz77rPz8/FSvXj29/PLLCg4O1uDBg311egAA4AKMCiYtW7ZURkaGFixYIMuy1KBBAw0aNEhDhw5VYGCgJCk2NlZpaWmaPXu2li9frmuuuUZTp05V7969PfqaMGGCqlevrpkzZ+rEiRO68cYbtXjx4rP+tQ4AADCDUcFk+PDhGj58+AXbdevWTd26dTtvm8DAQCUnJys5Odlb5QEAgDJm/BoTAABw5SCYAAAAYxBMAACAMQgmAADAGAQTAABgDIIJAAAwBsEEAAAYg2ACAACMQTABAADGIJgAAABjEEwAAIAxCCYAAMAYBBMAAGAMggkAADAGwQQAABiDYAIAAIxBMAEAAMYgmAAAAGMQTAAAgDEIJgAAwBgEEwAAYAyCCQAAMAbBBAAAGINgAgAAjEEwAQAAxiCYAAAAYxBMAACAMQgmAADAGAQTAABgDIIJAAAwBsEEAAAYg2ACAACMQTABAADGIJgAAABjEEwAAIAxCCYAAMAYBBMAAGAMggkAADAGwQQAABiDYAIAAIxBMAEAAMYgmAAAAGMQTAAAgDEIJgAAwBgEEwAAYAyCCQAAMAbBBAAAGCPA1wWc6cMPP9R7772n7777Ti6XS40bN1ZCQoLuuOMO2Ww2SVJCQoK+/PLLEs/NyMhQZGSk+3FOTo5SU1O1Zs0a5efnq2PHjpowYYLq1q1bbucDAAAujVHB5JVXXlGDBg2UkpKimjVr6osvvtDEiRN16NAhJSYmutvdeOONSk5O9nhuWFiYx+OkpCTt3r1bkydPVlBQkGbPnq1hw4ZpxYoVCggw6rQBAMD/Y9Q79Pz581WrVi334w4dOig7O1uLFy/Wo48+Kj+/03ee7Ha7oqOjz9nPtm3btGHDBqWnpys+Pl6SFB4erj59+uijjz5Snz59yvQ8AABA6Ri1xuTMUFKsWbNmOn78uE6ePHnR/axfv152u11xcXHubREREWrWrJnWr1/vlVoBAID3GRVMzuarr75SvXr1VKNGDfe2L7/8UtHR0YqKitJ9992nLVu2eDwnMzNT4eHh7nUpxSIiIpSZmVkudQMAgEtn1K2c/7V161ZlZGR4rCdp06aN+vfvryZNmujIkSNKT0/Xgw8+qNdff10xMTGSJJfLpeDg4BL9hYSE6Ntvv73sugICLpzn/P2Nz3yVVllde8bUd8ri2jOevsN4Vi7evvbGBpNDhw5pzJgxateunYYMGeLe/thjj3m0++Mf/6h+/frppZde0sKFC8u8Lj8/m2rWrF7mx0Hp2e1VfV0CvIwxrVwYz8rF2+NpZDBxuVwaNmyYQkNDlZaW5l70ejbVqlVT586d9a9//cu9zW6369ChQyXaOp1OhYSEXFZtRUWWXK4Lr3fx9/fjxecjLleuCguLvN4vY+o7ZTGmjKfvMJ6Vy8WOp91e9aJmV4wLJqdOndLDDz+snJwcLVmy5Ky3ZC4kIiJCmzZtkmVZHutM9u7dq6ZNm152jQUF3n/Tg/cUFhYxRpUMY1q5MJ6Vi7fH06ibcgUFBUpKSlJmZqYWLVqkevXqXfA5J0+e1GeffaaoqCj3tk6dOsnpdGrTpk3ubXv37tWOHTvUqVOnMqkdAABcPqNmTKZMmaJPP/1UKSkpOn78uL755hv3vubNm2v79u1atGiRevTooQYNGujIkSNavHixfvnlF7344ovutjExMYqPj9f48eOVnJysoKAgzZo1Sw6HQz179vTBmQEAgIthVDDZuHGjJGn69Okl9q1du1Z16tRRfn6+Zs2apezsbFWtWlUxMTGaMmWKWrZs6dF+9uzZSk1N1aRJk1RQUKD4+HhNmDCBT30FAMBgRr1Lf/LJJxdsk56eflF9BQcHa9q0aZo2bdrllgUAAMqJUWtMAADAlY1gAgAAjEEwAQAAxiCYAAAAYxBMAACAMQgmAADAGAQTAABgDIIJAAAwBsEEAAAYg2ACAACMQTABAADGIJgAAABjEEwAAIAxCCYAAMAYBBMAAGAMggkAADAGwQQAABiDYAIAAIxBMAEAAMYgmAAAAGMQTAAAgDEIJgAAwBgEEwAAYAyCCQAAMAbBBAAAGINgAgAAjEEwAQAAxiCYAAAAYxBMAACAMQgmAADAGAQTAABgDIIJAAAwBsEEAAAYg2ACAACMQTABAADGIJgAAABjEEwAAIAxCCYAAMAYBBMAAGAMggkAADAGwQQAABiDYAIAAIxBMAEAAMYodTBZtWqVDh48eM79Bw8e1KpVq0rbPQAAuAKVOpg89dRT2rZt2zn3b9++XU899VRpuwcAAFegUgcTy7LOu//kyZPy9/cvbfcAAOAKFHApjb///nt9//337sdbt25VYWFhiXYul0vvvPOOwsPDL79CAABwxbikYLJmzRrNnTtXkmSz2bRkyRItWbLkrG3tdrtmzJhx+RUCAIArxiUFkzvvvFN//OMfZVmWBg0apMcee0ydOnXyaGOz2VS1alU1atRIAQGX1L0+/PBDvffee/ruu+/kcrnUuHFjJSQk6I477pDNZnO3W7ZsmRYtWqT//ve/Cg8P15gxY9SlSxePvnJycpSamqo1a9YoPz9fHTt21IQJE1S3bt1LqgkAAJSfS0oOdevWdb+xv/baa4qMjFTt2rW9Vswrr7yiBg0aKCUlRTVr1tQXX3yhiRMn6tChQ0pMTJQkffDBB5o4caJGjBih9u3bKyMjQ4mJiXrzzTcVHR3t7ispKUm7d+/W5MmTFRQUpNmzZ2vYsGFasWLFJQcmAABQPkr9Dt22bVtv1iFJmj9/vmrVquV+3KFDB2VnZ2vx4sV69NFH5efnpzlz5qhv375KSkqSJLVv314//vij5s2bp4ULF0qStm3bpg0bNig9PV3x8fGSpPDwcPXp00cfffSR+vTp4/XaAQDA5busqYPPP/9cy5cv14EDB+RyuUr8pY7NZtOaNWsuur8zQ0mxZs2aaenSpTp58qR+++037du3T+PGjfNo06dPHz377LPKy8tTYGCg1q9fL7vdrri4OHebiIgINWvWTOvXryeYAABgqFIHk0WLFmnmzJmqXbu2WrZsKYfD4c263L766ivVq1dPNWrU0FdffSVJJf7aJzIyUvn5+Tpw4IAiIyOVmZmp8PBwj3Up0ulwkpmZedk1BQRc+K+s/f35UF1fKatrz5j6Tllce8bTdxjPysXb177UweS1115T+/bttWDBAlWpUsWbNblt3bpVGRkZSk5OliQ5nU5Jp//i50zFj4v3u1wuBQcHl+gvJCRE33777WXV5OdnU82a1S+rD5Qtu72qr0uAlzGmlQvjWbl4ezxLHUxcLpd69epVZqHk0KFDGjNmjNq1a6chQ4aUyTFKo6jIkst18oLt/P39ePH5iMuVq8LCIq/3y5j6TlmMKePpO4xn5XKx42m3V72o2ZVSB5OoqCjt3bu3tE8/L5fLpWHDhik0NFRpaWny8zt9IiEhIZJO/ylwnTp1PNqfud9ut+vQoUMl+nU6ne42l6OgwPtvevCewsIixqiSYUwrF8azcvH2eJb6xtDkyZP18ccf6/333/daMZJ06tQpPfzww8rJydGiRYs8bslERERIUol1IpmZmapSpYoaNmzobrd3794Si3H37t3r7gMAAJin1DMmSUlJKigo0JNPPqnJkyerfv367pmNYjabTe+9995F91lQUKCkpCRlZmbqzTffVL169Tz2N2zYUE2aNNHq1avVvXt39/aMjAx16NBBgYGBkqROnTrppZde0qZNm3TTTTdJOh1KduzYoYceeqi0pwwAAMpYqYNJaGioQkND1bhxY68VM2XKFH366adKSUnR8ePH9c0337j3NW/eXIGBgRo1apTGjh2rRo0aqV27dsrIyND27dv1xhtvuNvGxMQoPj5e48ePV3JysoKCgjRr1iw5HA717NnTa/UCAADvKnUwef31171ZhyRp48aNkqTp06eX2Ld27VqFhYWpX79+ys3N1cKFC7VgwQKFh4dr7ty5iomJ8Wg/e/ZspaamatKkSSooKFB8fLwmTJjAp74CAGAwo96lP/nkk4tqN2jQIA0aNOi8bYKDgzVt2jRNmzbNG6UBAIByUOpgsmXLlotq16ZNm9IeAgAAXGFKHUwSEhJKfLLq2ezcubO0hwAAAFeYy/rk1/9VWFiorKwsLV26VEVFRXriiScu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gBkqbTDp1KmTvvjiC7lcLve21atXy8/PT3FxcT6sDAAAnIvNsspimaDvOZ1O9e3bV+Hh4Xr44YfdH7B2yy238AFrAAAYqtIGE+n0R9I/88wz2rZtm6pXr67+/ftrzJgxCgwM9HVpAADgLCp1MAEAABVLpV1jAgAAKh6CCQAAMAbBBAAAGINgAgAAjEEwAQAAxiCYAAAAYxBMAACAMQgmV4g1a9bozTffLLE9JSVF/fr180FFFyctLU1ff/21r8swVkUZV5fLpbS0NO3evdvXpRjn4MGDSktL0+HDhz22b968WQ6HQ//n//wfH1V2fuf63sNpFWlcV65cqffff9/XZbgRTK4Qa9as0dtvv+3rMi7Z3LlztW3bNl+XYayKMq4ul0tz584lmJxFVlaW5s6dqyNHjvi6lEtSUb73fKUijes//vEP/fOf//R1GW4Bvi4AAK5ElmUpPz/f12XAyxjXy8eMiY/t2rVLw4YNU7t27dSqVSv16tVLCxcudO//6KOP1L9/f0VFRSk+Pl6pqan6/fff3ftXrlwph8OhY8eOefTbv39/paSkSDo9rf+Pf/xDu3btksPhkMPhcO8rtnnzZt12222Kjo7WwIED9e2337r3jR8/Xvfcc4/78bFjx3T99dfrjjvucG87ceKEbrjhBn344YfubXv27NEjjzyi1q1bKzo6WsOHD9f+/fs9jrt8+XL17dtXLVu2VLt27XT33Xdr+/btkiSHwyFJevbZZ911b968+dIusI9UhHGVTv8QTU9PV69evdSiRQt169ZNr7zyikebPXv2aMyYMercubNatWqlPn366O9//7uKioo82i1YsEA9evRQVFSU2rdvrwceeEAHDhzQwYMH1a1bN0nS6NGj3bUePHiwdBe3nBXfFjvftfz999+Vmpqq+Ph4RUVFqX///vr444/P2s+6det06623KioqSp988omGDBkiSRo4cKD72pzJ5XLpiSeeUExMjLp06eLxfbR161Y5HA6P19WIESPkcDi0a9cu97bHH39cw4cPdz/Oy8vTCy+8oC5duqhFixbq3bt3ian8830PX8z3nulMHtdi27Zt05AhQxQdHa3WrVvriSee0NGjRz3aPP/887rlllsUExOjjh076vHHHy8xS/PVV1/p3nvvVevWrRUTE6NbbrlF//jHPyRJCQkJ+vLLL/XZZ5+560xLSyv9hfUCZkx8bMSIEbr66qv117/+VTVq1ND+/ft16NAhSdLatWv12GOPqW/fvnriiSeUmZmpWbNm6eeff9acOXMu+hiPPvqojh07pszMTD3//POSpFq1arn3//LLL5o6daqGDx+u4OBgzZw5U4mJifr4449VpUoVtWnTRu+//75+//13BQUFaevWrQoMDNTOnTt1/Phx1ahRQ9u2bVNBQYHatGkjSTpw4IAGDx6s6667TtOnT5fNZtPf/vY3PfDAA1q9erUCAwO1ZcsW/fnPf9af/vQnde7cWadOndL27duVk5MjSVqyZInuuusuJSQkuNdLXHvttV657mWtIoyrJP31r3/VsmXLNGLECLVq1Upff/21nn/+eQUFBenuu++WJB05ckTh4eG65ZZbVL16de3cuVNpaWk6efKkEhMTJUmrVq3Siy++qMcee0zR0dHKycnRV199pRMnTigiIkJz585VYmKiHn/8cbVr106SVLdu3cu/0OXkQtdy7Nix+vzzz5WUlKSIiAi9++67GjVqlObNm+cOZdLpazl16lQ98sgj+sMf/qCaNWtq0qRJevrpp5WamqqIiIgSx/7LX/6i/v37a968eVqzZo2ef/55ORwOderUSS1btlRQUJC2bNmiRo0aqaioSF999ZV723XXXSdJ2rJlixISEtx9jh49Wl9//bVGjhypyMhIrVu3TuPGjZPdblfnzp0lnf97+ELfexWFqeMqnQ4lCQkJ6ty5s2bNmqXc3FzNnj1bjz76qJYsWeLu5+jRo3r44YdVt25dHTt2TIsXL1ZCQoI++OADBQQE6Pjx43r44YfVunVrvfDCCwoMDNTu3bvlcrncdYwbN05XXXWVkpOTJUn169cvy8t+YRZ85ujRo1bTpk2ttWvXnnX/bbfdZt11110e29555x2radOm1vfff29ZlmWtWLHCatq0qXX06FGPdrfeequVnJzsfpycnGz17du3xDGSk5Mth8Nh/fjjj+5t//73v62mTZtaW7ZssSzLsvbv3281bdrU2rx5s2VZljV16lTr8ccft9q2bWutW7fOsizLeuGFF6yePXu6+3jyySetbt26WadOnfI43+joaOuNN96wLMuyFi1aZLVt2/a816hp06bWokWLztvGNBVlXH/66SfL4XBY77zzjsdzn3vuOSsuLs4qLCws0W9RUZGVn59vzZ8/34qLi3NvnzJlijVgwICznq9lWdaBAwespk2bWh9++OE525jqQtdy586dVtOmTa23337b43l33XWXxzVJTk62mjZtan3zzTce7Yr72r59+1m3z5gxw72tqKjI6tKlizV+/Hj3tnvvvddKSUmxLMuyduzYYd1www3WxIkTraSkJMuyLGvfvn1W06ZNra+//tqyLMvatGmT1bRpU+vzzz/3OF5SUpJ1xx13WJZ14e/h4vM52/deRVERxvWuu+6yioqK3Nt27dplORwO67PPPjvrORUUFFiHDh3yGN/t27d7/Gw5m/vuu88aPnz4OfeXN27l+FDNmjXVoEEDvfDCC/rHP/7h/m1EOn1rZOfOnerVq5fHc/r06SPp9NSct9StW9f9m5X0/2clileTN2zYUPXr19eWLVsknZ4+btu2rWJjYz22Fc+WSNLGjRvVtWtX+fv7q6CgQAUFBbLb7WrevLl7qrR58+bKzs5WSkqKNm7cqNzcXK+dky9VlHH94osvJEk9e/Z0j1FBQYFuuukm/fLLL/r5558lnZ7OnjNnjvs2zQ033KBZs2bpl19+0YkTJySdHssdO3YoNTVVW7durXT32M93LYvH7Oabb/Z4Tu/evbVjxw6dPHnSvS00NFStWrW6pGPHx8e7v7bZbIqMjPT4njrzdbhlyxa1aNFCnTp18thWtWpVtWjRQtLp12ZoaKjat29fYtx37typwsLC834PVyamjmtubq6+/vpr3XzzzSosLHSPUZMmTfSHP/zB4y961q1bp8GDB6t169Zq3ry5e8Zl3759kqRGjRqpRo0amjx5sjIyMkrcHjYRt3J8yGazKT09XbNmzdLTTz+tkydP6oYbbtBTTz2lhg0byrIs1a5d2+M5wcHBCgwMlNPp9Foddrvd43HxNP+Zax7atGmjrVu36vjx4/r+++8VGxur3NxcrV69Wnl5edq+fbsGDRrkbv/bb7/p1Vdf1auvvlrieMX9d+jQQc8++6xee+01DR06VEFBQerVq5fGjx+v0NBQr51feaso4/rbb7/Jsiy1b9/+rM//+eef1aBBAz333HNatmyZRo4cqRYtWig4OFhr167V/Pnz9fvvv6t69eq6/fbbdeLECS1dulSvvPKKgoODddttt2ns2LG66qqrvHZOvnK+a+l0OlWlSpUS37NXX321LMtSTk6OqlWr5t52qYKDg0scu/h2pyS1bdtW8+fP1+HDh7V161bFxsYqNjZWv/76q/bt26etW7eqVatW7pp/++03ZWdn64Ybbjjr8X755RfVr1//nN/DZ/4CUtGZOq4ul0uFhYVKTU1VampqiecW/9Kwfft2Pfroo+rWrZuGDRum2rVry2az6c4773S/zkNCQrR48WLNmTNHTz75pAoLCxUbG6sJEyaUWPdiCoKJj4WHh2vOnDnKz8/Xtm3b9MILL2jEiBFav369bDZbiXSbk5OjvLw8hYSESJKCgoIkqcRvqMX3D72lTZs2mj59ujZv3qyaNWsqMjJSubm5ev755/Xvf/9beXl5io2NdbcPCQlR586dPRbNFqtevbr76/79+6t///46duyY1q5dq9TUVAUEBGjatGlerb+8VYRxDQkJkc1m01tvveX+gfy/5yBJq1ev1l133eWxeHLdunUebf38/HT//ffr/vvv1+HDh/XBBx9o5syZqlmzpkaOHOm1mk0UEhKi/Px8OZ1O9/hJ0q+//iqbzebxBmSz2bx+/OjoaFWpUkVbtmzR1q1bdccddyg0NFTXXXedtmzZoi1btui2227zqLdWrVpasGDBWfsrXityvu/hM1/DlZUvxzU4OFg2m00PP/ywunfvXmJ/zZo1JZ3+k+0aNWpo9uzZ8vM7fQMkKyurRPuWLVtq0aJFOnXqlDZv3qwZM2Zo5MiRWrNmjVfr9hZu5RiiSpUqatu2rYYPH67jx4/ryJEjatasmVavXu3RrvivXlq3bi1JqlevniQpMzPT3WbPnj3uRH1m/2fOgFyq2NhYnTx5Uq+88oo7gDRr1kxBQUFauHCh/vCHPygsLMzdvkOHDtq1a5eaN2+uqKgoj//OthCsVq1aGjRokOLi4jzO5XLr9jWTx7VDhw6SpOzs7BJjFBUVpRo1akg6/dvjmcGlsLBQH3zwwTn7rVevnv70pz/J4XC46z/bLFxlUTxm/zumq1evVvPmzd2/VZ/L5V6batWqqXnz5lqyZImys7Pd9bRp00bvvfeeDh486PFLw0033aRjx46pSpUqZx33wMDAEvX97/dw8fbKOJ7FfDmu1apVU3R0tDIzM886RsU/a0+dOqUqVap4BKPzfVDaVVddpc6dO+vuu+/WwYMH3bWZNpbMmPjQ999/rxkzZqhPnz5q2LChjh8/rpdfflkNGjRQo0aNlJiYqJEjR2rs2LG69dZbtXfvXs2aNUu9evVyT8G1atVKf/jDHzRt2jQ98cQTOn78uBYsWFBi+jEyMlIrVqzQP//5TzVu3Fg1a9b0CBIXEhkZqdq1a+vLL7/UhAkTJEn+/v668cYbtX79et1yyy0e7R977DENHDhQQ4cO1Z133qmrr75av/76q7788kvFxsaqX79+mjNnjrKzs9W2bVvVrl1bP/74oz7//HM98MAD7n4iIiK0du1axcbGqmrVqgoPD3e/YZqqooxreHi47r33Xj355JMaOnSoWrVqpfz8fO3bt0+bN2/WSy+9JOn0G9myZct07bXXqmbNmnrrrbeUl5fn0dekSZNkt9sVHR0tu92ur7/+Wt9//737L3vq1Kkju92uDz74QGFhYQoMDJTD4SjxJlgRXX/99erZs6emT5+uU6dOKTw8XO+99562bdvmvobn06RJE/n7+2vFihUKCAiQv7+/oqKiLqmG2NhYpaen64YbbnC/PmJjY/Xmm2+qSpUqiomJcbeNi4tTly5d9NBDD+mhhx6Sw+FQbm6udu/erZ9++kl//etfL/g9LF3+zxTT+Xpcn3zySd1///1KSkpS3759ZbfbdejQIX3xxRe6/fbb1a5dO8XFxenVV1/VM888ox49emjbtm169913Pfr57LPPtHz5cnXv3l3XXHONfv31V73xxhu68cYb3TOzERERWrVqlT755BPVqVNHdevWdf9y5AsEEx+qU6eOrr76ar388ss6fPiwgoODFRsbq+eee07+/v7q1q2bXnzxRc2bN0+PPvqoQkNDdeedd+qJJ55w91GlShXNnTtXkydP1ujRo9WoUSONHz9e06dP9zjWwIEDtX37dj3zzDPKzs7WgAEDSrS5kNjYWP3rX//yuMfcpk0brV+/vsR958aNG2vZsmWaPXu2pkyZopMnT6pOnTpq06aN+803KipKr776qj788EMdP35c9evX19ChQ/XII4+4+5k0aZKmTZumYcOG6dSpU3rttdfcf25qqoo0rhMmTFB4eLiWLFmiefPmqXr16goPD/dY8Ddx4kT95S9/0TPPPKOqVatqwIAB6tGjhzugSlJMTIyWLl2qZcuWKTc3Vw0bNtRTTz3lXnfk5+en1NRUvfDCC3rggQeUl5entWvXVpo3sueee04vvPCCFi5cqOzsbEVERGjOnDnq2rXrBZ9bq1YtTZo0SYsWLdJ7772n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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "insurance_dataset['region'].value_counts()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 241
        },
        "id": "2i0zlMupedID",
        "outputId": "ca33c32d-30ed-414f-a334-c9cbf5a0dbfb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "region\n",
              "southeast    364\n",
              "southwest    325\n",
              "northwest    325\n",
              "northeast    324\n",
              "Name: count, dtype: int64"
            ],
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>count</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>region</th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>southeast</th>\n",
              "      <td>364</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>southwest</th>\n",
              "      <td>325</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>northwest</th>\n",
              "      <td>325</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>northeast</th>\n",
              "      <td>324</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div><br><label><b>dtype:</b> int64</label>"
            ]
          },
          "metadata": {},
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Distribution of charges value\n",
        "plt.figure(figsize=(6,6))\n",
        "sns.displot(insurance_dataset['charges'])\n",
        "plt.title('charges Distribution')\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 540
        },
        "id": "x3LJvz4Hehy-",
        "outputId": "96f2df46-3141-44af-c306-ddbf85a4aa91"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 600x600 with 0 Axes>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 500x500 with 1 Axes>"
            ],
            "image/png": "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nO6E43QfnjBGgON0RS4dyJs3b8bvfvc7xMfHW81v3LgxZs2aZZmOi4vDww8/jNGjR2P79u3o27dvpbepUilo0MDxi8O0Wt9yl2nUKmg0arttaO580AIC/Bzebm2raJzuhON0H54wRoDjdCUuG8i3b9/G7t27kZycDLXafqh16dIFfn5+OHPmTJUC2WQS0Ony7dap1Spotb7Q6QpgNJqslqlUCgIC/GAwmmAwGO22Zbizvk5XYHPleXmEEHCwtEoqGqc74TjdhyeMEeA4ZeLoTpzLBvL27dtRWFiIJ554ota3bTA4/qYbjSabevMh69LQtJ+a93mrYTQJp74BGowm5Ny6XSuhDJQ9TnfEcboPTxgjwHG6EpcN5C1btqBZs2aIjo52qH737t3Iz89HZGRkDfes+nl7qaFWKVi64Thy9EV26wP9fTAmOQaKoji8R01ERHVLqkAuKCjA3r17AQCXL1+GXq9HZmYmgNLzwA0bNgQA3Lx5EwcPHsSoUaPKbGfevHlQFAUxMTHQarU4efIkli1bhrZt21ruc3ZFOfoi3NIV1nU3iIioBkgVyDdu3MArr7xiNc88/eGHH1qeupWRkQGDwVDu4erQ0FB88sknWL9+PQoLCxEUFIRBgwYhLS0NGo1UQyYiIgIgWSA3bdoUP/74o9265557Ds8991y5y5OTk5GcnFydXSMiIqpRrn/jFhERkRtgIBMREUmAgUxERCQBBjIREZEEGMhEREQSYCATERFJgIFMREQkAQYyERGRBBjIREREEmAgExERSYCBTEREJAEGMhERkQQYyERERBJgIBMREUmAgUxERCQBBjIREZEEGMhEREQSYCATERFJgIFMREQkAQYyERGRBBjIREREEmAgExERSYCBTEREJAEGMhERkQQYyERERBJgIBMREUmAgUxERCQBBjIREZEEGMhEREQSYCATERFJgIFMREQkAQYyERGRBDR13QGqOSqV4nCtEAJC1GBniIioQgxkN+Tro4HRJNCgQT2H1zEYTci5dZuhTERUR6QK5PPnz2PlypU4ceIEsrKyEBISgi1btljVpKam4siRIzbrpqenIzQ01DKdl5eHuXPnYseOHSgpKUHnzp0xbdo0NG7cuMbHUde8vdRQqxQs3XAcOfoiu/WB/j4YkxwDRVEgmMhERHVCqkDOysrC3r17ER0dDZPJVG44PPLI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wOnTp8tc9tBDD2HlypW13CMiIqKqcdlzyERERO6EgUxERCQBBjIREZEEGMhEREQSYCATERFJgIFMREQkAQYyERGRBBjIREREEmAgExERSYCBTEREJAEGMhERkQQYyERERBJgIBMREUmAgUxERCQBBjIREZEEGMhEREQSYCATERFJgIFMREQkAQYyERGRBBjIREREEmAgExERSYCBTEREJAEGMhERkQQYyERERBJgIBMREUmAgUxERCQBBjIREZEEGMhEREQSYCATERFJQFPXHSAqj0qlOFwrhIAQNdgZIqIaxkAm6fj6aGA0CTRoUM/hdQxGE3Ju3WYoE5HLYiCTdLy91FCrFCzdcBw5+iK79YH+PhiTHANFUSCYyETkohjIJK0cfRFu6QrruhtERLWCF3URERFJwOUC+fPPP0d4eLjNf2+99ZZV3YYNG9C7d29ERkaif//+2L17dx31mIiIyD6XPWS9YsUK1K9f3zIdFBRk+fuXX36J6dOn46WXXkLHjh2Rnp6OcePG4aOPPkJMTEwd9JaIiKhiLhvIbdq0QcOGDctctnDhQvTr1w8TJkwAAHTs2BE//fQTlixZguXLl9diL4mIiBzjcoes7bl48SLOnTuHPn36WM3v27cvDh48iOLi4jrqGRERUflcNpCTkpIQERGB7t27Y9myZTAajQCA7OxsAECLFi2s6kNDQ1FSUoKLFy/Wel+JiIjscblD1o0aNcL48eMRHR0NRVGwa9cuzJ8/H1evXsWMGTOQm5sLANBqtVbrmafNy6tCo7H/PUatVln9eTfzE6gURYGi2H8alblExnqYyxVAQdnr1nx/Sms0GhVMppq5D7mi99OdeMI4PWGMAMfpilwukDt37ozOnTtbphMSEuDj44M1a9bgpZdeqvHtq1SKU0+Q0mp9y12mUaug0ajttqG580GTsl6tvvP38terrf4EBPjZra2qit5Pd+IJ4/SEMQIcpytxuUAuS58+ffDBBx/g+++/R0BAAAAgLy8PjRo1stTodDoAsCyvLJNJQKfLt1unVqug1fpCpyuA0WiyWqZSKQgI8IPBaILBYLTbluHO+lLWG43QqNUwGI1AOTuntdWf3Nz8Gt1DLu/9dCeeME5PGCPAccrE0Z04twjku4WEhAAoPZds/rt52svLC8HBwVXehsHg+JtuNJps6s2HrEt/EMF+gJhLZKy3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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Data pre - Proccessing**"
      ],
      "metadata": {
        "id": "3gKRUozLgF8B"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Encoding the Categorical features**"
      ],
      "metadata": {
        "id": "4R_j4crlgSpa"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# encoding six columns\n",
        "insurance_dataset.replace({'sex':{'male':0,'female':1}},inplace=True)\n",
        "# encoding smoker column\n",
        "\n",
        "insurance_dataset.replace({'smoker':{'yes':0,'no':1}},inplace=True)\n",
        "\n",
        "\n",
        "# encoding region column\n",
        "insurance_dataset.replace({'region':{'southeast':0,'southwest':1,'northeast':2,'northwest':3}},inplace=True)"
      ],
      "metadata": {
        "id": "-tbMwWLwgdeI"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "insurance_dataset.head(10)\n",
        "insurance_dataset.tail(10)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 363
        },
        "id": "UnKd-px5gN7h",
        "outputId": "725b9b84-f43e-47fd-8a7f-159245688bef"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "      age  sex     bmi  children  smoker  region      charges\n",
              "1328   23    1  24.225         2       1       2  22395.74424\n",
              "1329   52    0  38.600         2       1       1  10325.20600\n",
              "1330   57    1  25.740         2       1       0  12629.16560\n",
              "1331   23    1  33.400         0       1       1  10795.93733\n",
              "1332   52    1  44.700         3       1       1  11411.68500\n",
              "1333   50    0  30.970         3       1       3  10600.54830\n",
              "1334   18    1  31.920         0       1       2   2205.98080\n",
              "1335   18    1  36.850         0       1       0   1629.83350\n",
              "1336   21    1  25.800         0       1       1   2007.94500\n",
              "1337   61    1  29.070         0       0       3  29141.36030"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-046adb9e-cca6-405f-b36f-b4cefa2d7417\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>age</th>\n",
              "      <th>sex</th>\n",
              "      <th>bmi</th>\n",
              "      <th>children</th>\n",
              "      <th>smoker</th>\n",
              "      <th>region</th>\n",
              "      <th>charges</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>1328</th>\n",
              "      <td>23</td>\n",
              "      <td>1</td>\n",
              "      <td>24.225</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>22395.74424</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1329</th>\n",
              "      <td>52</td>\n",
              "      <td>0</td>\n",
              "      <td>38.600</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>10325.20600</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1330</th>\n",
              "      <td>57</td>\n",
              "      <td>1</td>\n",
              "      <td>25.740</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>12629.16560</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1331</th>\n",
              "      <td>23</td>\n",
              "      <td>1</td>\n",
              "      <td>33.400</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>10795.93733</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1332</th>\n",
              "      <td>52</td>\n",
              "      <td>1</td>\n",
              "      <td>44.700</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>11411.68500</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1333</th>\n",
              "      <td>50</td>\n",
              "      <td>0</td>\n",
              "      <td>30.970</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>10600.54830</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1334</th>\n",
              "      <td>18</td>\n",
              "      <td>1</td>\n",
              "      <td>31.920</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>2205.98080</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1335</th>\n",
              "      <td>18</td>\n",
              "      <td>1</td>\n",
              "      <td>36.850</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1629.83350</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1336</th>\n",
              "      <td>21</td>\n",
              "      <td>1</td>\n",
              "      <td>25.800</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>2007.94500</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1337</th>\n",
              "      <td>61</td>\n",
              "      <td>1</td>\n",
              "      <td>29.070</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>29141.36030</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-046adb9e-cca6-405f-b36f-b4cefa2d7417')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-046adb9e-cca6-405f-b36f-b4cefa2d7417 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-046adb9e-cca6-405f-b36f-b4cefa2d7417');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-cf94080e-de5e-4f1e-87cd-0be4ac7d7267\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-cf94080e-de5e-4f1e-87cd-0be4ac7d7267')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-cf94080e-de5e-4f1e-87cd-0be4ac7d7267 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "summary": "{\n  \"name\": \"insurance_dataset\",\n  \"rows\": 10,\n  \"fields\": [\n    {\n      \"column\": \"age\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 18,\n        \"min\": 18,\n        \"max\": 61,\n        \"num_unique_values\": 7,\n        \"samples\": [\n          23,\n          52,\n          21\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"sex\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          0,\n          1\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"bmi\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 6.479886508779816,\n        \"min\": 24.225,\n        \"max\": 44.7,\n        \"num_unique_values\": 10,\n        \"samples\": [\n          25.8,\n          38.6\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"children\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1,\n        \"min\": 0,\n        \"max\": 3,\n        \"num_unique_values\": 3,\n        \"samples\": [\n          2,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"smoker\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          0,\n          1\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"region\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1,\n        \"min\": 0,\n        \"max\": 3,\n        \"num_unique_values\": 4,\n        \"samples\": [\n          1,\n          3\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"charges\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 8866.014402476827,\n        \"min\": 1629.8335,\n        \"max\": 29141.3603,\n        \"num_unique_values\": 10,\n        \"samples\": [\n          2007.945,\n          10325.206\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Splitting the Features and Targets"
      ],
      "metadata": {
        "id": "JdbQxo0dk2uK"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "x = insurance_dataset.drop(columns='charges',axis=1)\n",
        "y = insurance_dataset['charges']"
      ],
      "metadata": {
        "id": "Uhth_1t1lFBB"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(x)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zHIlhjcifKYq",
        "outputId": "9df94871-88ae-4003-d1ee-48644cfc38a1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "      age  sex     bmi  children  smoker  region\n",
            "0      19    1  27.900         0       0       1\n",
            "1      18    0  33.770         1       1       0\n",
            "2      28    0  33.000         3       1       0\n",
            "3      33    0  22.705         0       1       3\n",
            "4      32    0  28.880         0       1       3\n",
            "...   ...  ...     ...       ...     ...     ...\n",
            "1333   50    0  30.970         3       1       3\n",
            "1334   18    1  31.920         0       1       2\n",
            "1335   18    1  36.850         0       1       0\n",
            "1336   21    1  25.800         0       1       1\n",
            "1337   61    1  29.070         0       0       3\n",
            "\n",
            "[1338 rows x 6 columns]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(y)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ePV98TWLmhob",
        "outputId": "c2490a58-4bcd-42a2-f6c4-22914a294afb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0       16884.92400\n",
            "1        1725.55230\n",
            "2        4449.46200\n",
            "3       21984.47061\n",
            "4        3866.85520\n",
            "           ...     \n",
            "1333    10600.54830\n",
            "1334     2205.98080\n",
            "1335     1629.83350\n",
            "1336     2007.94500\n",
            "1337    29141.36030\n",
            "Name: charges, Length: 1338, dtype: float64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Splitting the data into Traning data & Testing data"
      ],
      "metadata": {
        "id": "wyfCsQqfmuD2"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "x_train, x_test ,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=2)"
      ],
      "metadata": {
        "id": "8Eepho0ym5z0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(x.shape,x_train.shape,x_test.shape)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "w_Dx792DmjBJ",
        "outputId": "34955036-9989-490e-bb00-ab28ee8f1426"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(1338, 6) (1070, 6) (268, 6)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Model Traning\n",
        "\n",
        "Linear Regression"
      ],
      "metadata": {
        "id": "giSXOXfGoXAk"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Loading the Linear Regression Mode\n",
        "Regressor = LinearRegression()"
      ],
      "metadata": {
        "id": "ltdEOBdTolnb"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "Regressor.fit(x_train,y_train)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 75
        },
        "id": "cSCoAytDoWRT",
        "outputId": "2d828140-7921-4831-8f65-bc43a6f8fca7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "LinearRegression()"
            ],
            "text/html": [
              "<style>#sk-container-id-1 {color: black;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>LinearRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">LinearRegression</label><div class=\"sk-toggleable__content\"><pre>LinearRegression()</pre></div></div></div></div></div>"
            ]
          },
          "metadata": {},
          "execution_count": 27
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Prediction on traning data\n",
        "training_data_prediction = Regressor.predict(x_train)"
      ],
      "metadata": {
        "id": "HZj-xBCeshf5"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# R squared value\n",
        "r2_train = r2_score(y_train,training_data_prediction)\n",
        "print('R squared vale :',r2_train)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EGsF3TBbtKYL",
        "outputId": "9c236615-377d-4aca-cf41-dcbe6a28305b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "R squared vale : 0.751505643411174\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Prediction on test data\n",
        "test_data_prediction = Regressor.predict(x_test)"
      ],
      "metadata": {
        "id": "4FMZHxYItvwK"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# R Squared Value\n",
        "from sklearn import metrics\n",
        "r2_test = metrics.r2_score(y_test,test_data_prediction)\n",
        "print('R squared vale :',r2_test)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rDEEBb7MvDh-",
        "outputId": "c770287a-3086-4438-a7be-4634ae09078f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "R squared vale : 0.7447273869684076\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Building a Predictive System"
      ],
      "metadata": {
        "id": "qG_fTGLGxtmd"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "input_data = (31,1,25.74,0,1,0)\n",
        "\n",
        "# changing input data to a numpy arry\n",
        "input_data_as_numpy_array = np.asarray(input_data)\n",
        "\n",
        "# reshape the array\n",
        "input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)\n",
        "\n",
        "prediction = Regressor.predict(input_data_reshaped)\n",
        "print(prediction)\n",
        "\n",
        "print('The insurance cost is USD ',prediction[0])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CXH0rT5rxs3D",
        "outputId": "c8dcbfec-2b7c-4dce-b3e4-c3f5fe6305a5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[3760.0805765]\n",
            "The insurance cost is USD  3760.080576496057\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.10/dist-packages/sklearn/base.py:465: UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names\n",
            "  warnings.warn(\n"
          ]
        }
      ]
    }
  ]
}