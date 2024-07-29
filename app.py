# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import subprocess
# import pandas as pd
# from sqlalchemy import create_engine
# from sqlalchemy.engine import URL
#
# app = Flask(__name__)
# CORS(app)
#
#
# class Analise:
#     def __init__(self):
#         self.server = 'DBDEV'
#         self.database = 'JDE_CRP'
#         self.username = 'consultas_diretas'
#         self.password = 'c_diretas'
#
#     def cria_Conn(self):
#         connection_string = (
#             f"DRIVER={{SQL Server}};"
#             f"SERVER={self.server};"
#             f"DATABASE={self.database};"
#             f"UID={self.username};"
#             f"PWD={self.password}"
#         )
#         connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
#         engine = create_engine(connection_url)
#         return engine
#
#     def extrair_dados(self, SEQ_KEY):
#         query = f"""
#         SELECT
#             SEQ_KEY, ORDEM, VARIACAO_IMXIC = ABS(VARIACAO_IMXIC), DIF_CUSTO_P_x_R, MAT_DIF_PERCENTUAL,
#             TAXA_MAQUINA_FIXA, TAXA_MO_FIXA, TAXA_FIXA_VAR_MO, MO_VALOR, HR_MAQ_VALOR,
#             HR_EXC_VLR, HR_CONFIG_VLR, MO_VARIACAO, EXTERNA_OPERACAO
#         FROM  CRPDTA.FNML481
#         WHERE SEQ_KEY = {SEQ_KEY}
#         ORDER BY ORDEM, SEQ_KEY
#         """
#         engine = self.cria_Conn()
#         if engine:
#             df = pd.read_sql(query, engine)
#             engine.dispose()
#             return df
#         else:
#             return None
#
#
# @app.route('/get_variations', methods=['POST'])
# def get_variations():
#     data = request.json
#     seq_key = data.get('seq_key')
#
#     if not seq_key:
#         return jsonify({"error": "SEQ_KEY is required"}), 400
#
#     analise = Analise()
#     data = analise.extrair_dados(seq_key)
#     if data is not None:
#         return data.to_json(orient="records")
#     else:
#         return jsonify({"error": "Error fetching data from the database"}), 500
#
#
# @app.route('/submit_justification', methods=['POST'])
# def submit_justification():
#     data = request.json
#     seq_key = data.get('seq_key')
#     justification = data.get('justification')
#
#     if not seq_key or not justification:
#         return jsonify({"error": "SEQ_KEY and justification are required"}), 400
#
#     try:
#         result = subprocess.run(['./AI_WO_Approval.exe', str(seq_key), justification], capture_output=True, text=True)
#         return jsonify({"output": result.stdout, "error": result.stderr})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

#
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import subprocess
# import pandas as pd
# from sqlalchemy import create_engine
# from sqlalchemy.engine import URL
# import os
#
# app = Flask(__name__)
# CORS(app)
#
#
# class Analise:
#     def __init__(self):
#         self.server = 'DBDEV'
#         self.database = 'JDE_CRP'
#         self.username = 'consultas_diretas'
#         self.password = 'c_diretas'
#
#     def cria_Conn(self):
#         connection_string = (
#             f"DRIVER={{SQL Server}};"
#             f"SERVER={self.server};"
#             f"DATABASE={self.database};"
#             f"UID={self.username};"
#             f"PWD={self.password}"
#         )
#         connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
#         engine = create_engine(connection_url)
#         return engine
#
#     def extrair_dados(self, SEQ_KEY):
#         query = f"""
#         SELECT
#             SEQ_KEY, ORDEM, VARIACAO_IMXIC = ABS(VARIACAO_IMXIC), DIF_CUSTO_P_x_R, MAT_DIF_PERCENTUAL,
#             TAXA_MAQUINA_FIXA, TAXA_MO_FIXA, TAXA_FIXA_VAR_MO, MO_VALOR, HR_MAQ_VALOR,
#             HR_EXC_VLR, HR_CONFIG_VLR, MO_VARIACAO, EXTERNA_OPERACAO
#         FROM  CRPDTA.FNML481
#         WHERE SEQ_KEY = {SEQ_KEY}
#         ORDER BY ORDEM, SEQ_KEY
#         """
#         engine = self.cria_Conn()
#         if engine:
#             df = pd.read_sql(query, engine)
#             engine.dispose()
#             return df
#         else:
#             return None
#
#
# @app.route('/get_variations', methods=['POST'])
# def get_variations():
#     data = request.json
#     seq_key = data.get('seq_key')
#
#     if not seq_key:
#         return jsonify({"error": "SEQ_KEY is required"}), 400
#
#     analise = Analise()
#     data = analise.extrair_dados(seq_key)
#     if data is not None:
#         return data.to_json(orient="records")
#     else:
#         return jsonify({"error": "Error fetching data from the database"}), 500
#
#
# @app.route('/submit_justification', methods=['POST'])
# def submit_justification():
#     data = request.json
#     seq_key = data.get('seq_key')
#     justification = data.get('justification')
#
#     if not seq_key or not justification:
#         return jsonify({"error": "SEQ_KEY and justification are required"}), 400
#
#     try:
#         # Supondo que o executável está na mesma pasta que o app.py
#         executable_path = os.path.join(os.getcwd(), 'AI_WO_Approval.exe')
#         print(f"Received justification: {justification}")
#         print(f"Executing: {executable_path} {seq_key} {justification}")
#         result = subprocess.run([executable_path, str(seq_key), justification], capture_output=True, text=True)
#         print(f"Output: {result.stdout}")
#         print(f"Error: {result.stderr}")
#         return jsonify({"output": result.stdout, "error": result.stderr})
#     except Exception as e:
#         print(f"Exception: {e}")
#         return jsonify({"error": str(e)}), 500
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
#
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import subprocess
# import pandas as pd
# from sqlalchemy import create_engine
# from sqlalchemy.engine import URL
# import os
#
# app = Flask(__name__)
# CORS(app)
#
#
# class Analise:
#     def __init__(self):
#         self.server = 'DBDEV'
#         self.database = 'JDE_CRP'
#         self.username = 'consultas_diretas'
#         self.password = 'c_diretas'
#
#     def cria_Conn(self):
#         connection_string = (
#             f"DRIVER={{SQL Server}};"
#             f"SERVER={self.server};"
#             f"DATABASE={self.database};"
#             f"UID={self.username};"
#             f"PWD={self.password}"
#         )
#         connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
#         engine = create_engine(connection_url)
#         return engine
#
#     def extrair_dados(self, SEQ_KEY):
#         query = f"""
#         SELECT
#             SEQ_KEY, ORDEM, VARIACAO_IMXIC = ABS(VARIACAO_IMXIC), DIF_CUSTO_P_x_R, MAT_DIF_PERCENTUAL,
#             TAXA_MAQUINA_FIXA, TAXA_MO_FIXA, TAXA_FIXA_VAR_MO, MO_VALOR, HR_MAQ_VALOR,
#             HR_EXC_VLR, HR_CONFIG_VLR, MO_VARIACAO, EXTERNA_OPERACAO
#         FROM  CRPDTA.FNML481
#         WHERE SEQ_KEY = {SEQ_KEY}
#         ORDER BY ORDEM, SEQ_KEY
#         """
#         engine = self.cria_Conn()
#         if engine:
#             df = pd.read_sql(query, engine)
#             engine.dispose()
#             return df
#         else:
#             return None
#
#     def extrair_dados_agente(self, SEQ_KEY):
#         query = f"""
#         SELECT
#             [CHAVE SEQUENCIA] = A.GFN001,
#             [ORDEM DE PRODUCAO] = A.GFDOCO,
#             [SEQUENCIA REGISTRO] = A.GFN002,
#             [ANALISE ML] = CASE
#                 WHEN GFN003 = 0 THEN UPPER('Aprovação Requer Justificativa Plausivel da Fabrica')
#                 WHEN GFN003 = 1 THEN UPPER('Ordem Não Aprovavada: Limites fora da Faixa de Aceitação')
#                 WHEN GFN003 = 2 THEN UPPER('Considerável Probabilidade do Analista Humano de Custos Aprovar Ordem')
#                 WHEN GFN003 = 3 THEN UPPER('Ordem Não Aprovavada: Limites fora da Faixa de Aceitação')
#                 END,
#             [DECISAO DO AGENTE] = UPPER(A.GFDES1),
#             [JUSTIFICATIVA DO AGENTE] = UPPER(A.GFNOTTE)
#         FROM CRPDTA.FN31112Z A
#         WHERE
#             A.GFN002 = (SELECT MAX(B.GFN002) FROM CRPDTA.FN31112Z B WHERE B.GFN001 = A.GFN001) AND
#             A.GFN001 = {SEQ_KEY}
#         """
#         engine = self.cria_Conn()
#         if engine:
#             df = pd.read_sql(query, engine)
#             engine.dispose()
#             return df
#         else:
#             return None
#
#
# @app.route('/get_variations', methods=['POST'])
# def get_variations():
#     data = request.json
#     seq_key = data.get('seq_key')
#
#     if not seq_key:
#         return jsonify({"error": "SEQ_KEY is required"}), 400
#
#     analise = Analise()
#     data = analise.extrair_dados(seq_key)
#     if data is not None:
#         return data.to_json(orient="records")
#     else:
#         return jsonify({"error": "Error fetching data from the database"}), 500
#
#
# @app.route('/get_agent_analysis', methods=['POST'])
# def get_agent_analysis():
#     data = request.json
#     seq_key = data.get('seq_key')
#
#     if not seq_key:
#         return jsonify({"error": "SEQ_KEY is required"}), 400
#
#     analise = Analise()
#     data = analise.extrair_dados_agente(seq_key)
#     if data is not None:
#         return data.to_json(orient="records")
#     else:
#         return jsonify({"error": "Error fetching data from the database"}), 500
#
#
# @app.route('/submit_justification', methods=['POST'])
# def submit_justification():
#     data = request.json
#     seq_key = data.get('seq_key')
#     justification = data.get('justification', '')
#
#     if not seq_key:
#         return jsonify({"error": "SEQ_KEY is required"}), 400
#
#     try:
#         executable_path = os.path.join(os.getcwd(), 'AI_WO_Approval.exe')
#         print(f"Received justification: {justification}")
#         print(f"Executing: {executable_path} {seq_key} {justification}")
#         result = subprocess.run([executable_path, str(seq_key), justification], capture_output=True, text=True)
#         print(f"Output: {result.stdout}")
#         print(f"Error: {result.stderr}")
#         return jsonify({"output": result.stdout, "error": result.stderr})
#     except Exception as e:
#         print(f"Exception: {e}")
#         return jsonify({"error": str(e)}), 500
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
#

#
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import subprocess
# import pandas as pd
# from sqlalchemy import create_engine
# from sqlalchemy.engine import URL
# import os
#
# app = Flask(__name__)
# CORS(app)
#
#
# class Analise:
#     def __init__(self):
#         self.server = 'DBDEV'
#         self.database = 'JDE_CRP'
#         self.username = 'consultas_diretas'
#         self.password = 'c_diretas'
#
#     def cria_Conn(self):
#         connection_string = (
#             f"DRIVER={{SQL Server}};"
#             f"SERVER={self.server};"
#             f"DATABASE={self.database};"
#             f"UID={self.username};"
#             f"PWD={self.password}"
#         )
#         connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
#         engine = create_engine(connection_url)
#         return engine
#
#     def extrair_dados(self, SEQ_KEY):
#         query = f"""
#         SELECT
#             SEQ_KEY, ORDEM, VARIACAO_IMXIC = ABS(VARIACAO_IMXIC), DIF_CUSTO_P_x_R, MAT_DIF_PERCENTUAL,
#             TAXA_MAQUINA_FIXA, TAXA_MO_FIXA, TAXA_FIXA_VAR_MO, MO_VALOR, HR_MAQ_VALOR,
#             HR_EXC_VLR, HR_CONFIG_VLR, MO_VARIACAO, EXTERNA_OPERACAO
#         FROM  CRPDTA.FNML481
#         WHERE SEQ_KEY = {SEQ_KEY}
#         ORDER BY ORDEM, SEQ_KEY
#         """
#         engine = self.cria_Conn()
#         if engine:
#             df = pd.read_sql(query, engine)
#             engine.dispose()
#             return df
#         else:
#             return None
#
#     def extrair_dados_agente(self, SEQ_KEY):
#         query = f"""
#         SELECT
#             [CHAVE SEQUENCIA] = A.GFN001,
#             [ORDEM DE PRODUCAO] = A.GFDOCO,
#             [SEQUENCIA REGISTRO] = A.GFN002,
#             [ANALISE ML] = CASE
#                 WHEN GFN003 = 0 THEN 'Aprovação Requer Justificativa Plausivel da Fabrica'
#                 WHEN GFN003 = 1 THEN 'Ordem Não Aprovada: Limites fora da Faixa de Aceitação'
#                 WHEN GFN003 = 2 THEN 'Considerável Probabilidade do Analista Humano de Custos Aprovar Ordem'
#                 WHEN GFN003 = 3 THEN 'Ordem Não Aprovada: Limites fora da Faixa de Aceitação'
#                 END,
#             [DECISAO DO AGENTE] = A.GFDES1,
#             [JUSTIFICATIVA DO AGENTE] = A.GFNOTTE
#         FROM CRPDTA.FN31112Z A
#         WHERE
#             A.GFN002 = (SELECT MAX(B.GFN002) FROM CRPDTA.FN31112Z B WHERE B.GFN001 = A.GFN001) AND
#             A.GFN001 = {SEQ_KEY}
#         """
#         engine = self.cria_Conn()
#         if engine:
#             df = pd.read_sql(query, engine)
#             engine.dispose()
#             return df
#         else:
#             return None
#
#
# @app.route('/get_variations', methods=['POST'])
# def get_variations():
#     data = request.json
#     seq_key = data.get('seq_key')
#
#     if not seq_key:
#         return jsonify({"error": "SEQ_KEY is required"}), 400
#
#     analise = Analise()
#     data = analise.extrair_dados(seq_key)
#     if data is not None:
#         return data.to_json(orient="records")
#     else:
#         return jsonify({"error": "Error fetching data from the database"}), 500
#
#
# @app.route('/get_agent_analysis', methods=['POST'])
# def get_agent_analysis():
#     data = request.json
#     seq_key = data.get('seq_key')
#
#     if not seq_key:
#         return jsonify({"error": "SEQ_KEY is required"}), 400
#
#     analise = Analise()
#     data = analise.extrair_dados_agente(seq_key)
#     if data is not None:
#         return data.to_json(orient="records")
#     else:
#         return jsonify({"error": "Error fetching data from the database"}), 500
#
#
# @app.route('/submit_justification', methods=['POST'])
# def submit_justification():
#     data = request.json
#     seq_key = data.get('seq_key')
#     justification = data.get('justification', '')
#
#     if not seq_key:
#         return jsonify({"error": "SEQ_KEY is required"}), 400
#
#     try:
#         executable_path = os.path.join(os.getcwd(), 'AI_WO_Approval.exe')
#         print(f"Received justification: {justification}")
#         print(f"Executing: {executable_path} {seq_key} {justification}")
#         result = subprocess.run([executable_path, str(seq_key), justification], capture_output=True, text=True)
#         print(f"Output: {result.stdout}")
#         print(f"Error: {result.stderr}")
#         return jsonify({"output": result.stdout, "error": result.stderr})
#     except Exception as e:
#         print(f"Exception: {e}")
#         return jsonify({"error": str(e)}), 500
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

#
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import subprocess
# import pandas as pd
# from sqlalchemy import create_engine
# from sqlalchemy.engine import URL
# import os
# import json
#
# app = Flask(__name__)
# CORS(app)
#
#
# class Analise:
#     def __init__(self):
#         self.server = 'DBDEV'
#         self.database = 'JDE_CRP'
#         self.username = 'consultas_diretas'
#         self.password = 'c_diretas'
#
#     def cria_Conn(self):
#         connection_string = (
#             f"DRIVER={{SQL Server}};"
#             f"SERVER={self.server};"
#             f"DATABASE={self.database};"
#             f"UID={self.username};"
#             f"PWD={self.password}"
#         )
#         connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
#         engine = create_engine(connection_url)
#         return engine
#
#     def extrair_dados(self, SEQ_KEY):
#         query = f"""
#         SELECT
#             SEQ_KEY, ORDEM, VARIACAO_IMXIC = ABS(VARIACAO_IMXIC), DIF_CUSTO_P_x_R, MAT_DIF_PERCENTUAL,
#             TAXA_MAQUINA_FIXA, TAXA_MO_FIXA, TAXA_FIXA_VAR_MO, MO_VALOR, HR_MAQ_VALOR,
#             HR_EXC_VLR, HR_CONFIG_VLR, MO_VARIACAO, EXTERNA_OPERACAO
#         FROM  CRPDTA.FNML481
#         WHERE SEQ_KEY = {SEQ_KEY}
#         ORDER BY ORDEM, SEQ_KEY
#         """
#         engine = self.cria_Conn()
#         if engine:
#             df = pd.read_sql(query, engine)
#             engine.dispose()
#             return df
#         else:
#             return None
#
#     def extrair_dados_agente(self, SEQ_KEY):
#         query = f"""
#         SELECT
#             [CHAVE SEQUENCIA] = A.GFN001,
#             [ORDEM DE PRODUCAO] = A.GFDOCO,
#             [SEQUENCIA REGISTRO] = A.GFN002,
#             [ANALISE ML] = CASE
#                 WHEN GFN003 = 0 THEN 'Aprovação Requer Justificativa Plausivel da Fabrica'
#                 WHEN GFN003 = 1 THEN 'Ordem Não Aprovada: Limites fora da Faixa de Aceitação'
#                 WHEN GFN003 = 2 THEN 'Considerável Probabilidade do Analista Humano de Custos Aprovar Ordem'
#                 WHEN GFN003 = 3 THEN 'Ordem Não Aprovada: Limites fora da Faixa de Aceitação'
#                 END,
#             [DECISAO DO AGENTE] = A.GFDES1,
#             [JUSTIFICATIVA DO AGENTE] = A.GFNOTTE,
#             [VALORES EXCEDENTES] = A.GFANSR
#         FROM CRPDTA.FN31112Z A
#         WHERE
#             A.GFN002 = (SELECT MAX(B.GFN002) FROM CRPDTA.FN31112Z B WHERE B.GFN001 = A.GFN001) AND
#             A.GFN001 = {SEQ_KEY}
#         """
#         engine = self.cria_Conn()
#         if engine:
#             df = pd.read_sql(query, engine)
#             engine.dispose()
#             return df
#         else:
#             return None
#
#
# @app.route('/get_variations', methods=['POST'])
# def get_variations():
#     data = request.json
#     seq_key = data.get('seq_key')
#
#     if not seq_key:
#         return jsonify({"error": "SEQ_KEY is required"}), 400
#
#     analise = Analise()
#     data = analise.extrair_dados(seq_key)
#     if data is not None:
#         return data.to_json(orient="records")
#     else:
#         return jsonify({"error": "Error fetching data from the database"}), 500
#
#
# @app.route('/get_agent_analysis', methods=['POST'])
# def get_agent_analysis():
#     data = request.json
#     seq_key = data.get('seq_key')
#
#     if not seq_key:
#         return jsonify({"error": "SEQ_KEY is required"}), 400
#
#     analise = Analise()
#     data = analise.extrair_dados_agente(seq_key)
#     if data is not None:
#         return data.to_json(orient="records")
#     else:
#         return jsonify({"error": "Error fetching data from the database"}), 500
#
#
# @app.route('/submit_justification', methods=['POST'])
# def submit_justification():
#     data = request.json
#     seq_key = data.get('seq_key')
#     justification = data.get('justification', '')
#
#     if not seq_key:
#         return jsonify({"error": "SEQ_KEY is required"}), 400
#
#     try:
#         executable_path = os.path.join(os.getcwd(), 'AI_WO_Approval.exe')
#         print(f"Received justification: {justification}")
#         print(f"Executing: {executable_path} {seq_key} {justification}")
#         result = subprocess.run([executable_path, str(seq_key), justification], capture_output=True, text=True)
#         print(f"Output: {result.stdout}")
#         print(f"Error: {result.stderr}")
#         return jsonify({"output": result.stdout, "error": result.stderr})
#     except Exception as e:
#         print(f"Exception: {e}")
#         return jsonify({"error": str(e)}), 500
#
#
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import os
import json

app = Flask(__name__)
CORS(app)


class Analise:
    def __init__(self):
        self.server = 'DBDEV'
        self.database = 'JDE_CRP'
        self.username = 'consultas_diretas'
        self.password = 'c_diretas'

    def cria_Conn(self):
        connection_string = (
            f"DRIVER={{SQL Server}};"
            f"SERVER={self.server};"
            f"DATABASE={self.database};"
            f"UID={self.username};"
            f"PWD={self.password}"
        )
        connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
        engine = create_engine(connection_url)
        return engine

    def extrair_dados(self, SEQ_KEY):
        query = f"""
        SELECT 
            SEQ_KEY, ORDEM, VARIACAO_IMXIC = ABS(VARIACAO_IMXIC), DIF_CUSTO_P_x_R, MAT_DIF_PERCENTUAL, 
            TAXA_MAQUINA_FIXA, TAXA_MO_FIXA, TAXA_FIXA_VAR_MO, MO_VALOR, HR_MAQ_VALOR, 
            HR_EXC_VLR, HR_CONFIG_VLR, MO_VARIACAO, EXTERNA_OPERACAO 
        FROM  CRPDTA.FNML481
        WHERE SEQ_KEY = {SEQ_KEY}
        ORDER BY ORDEM, SEQ_KEY
        """
        engine = self.cria_Conn()
        if engine:
            df = pd.read_sql(query, engine)
            engine.dispose()
            return df
        else:
            return None

    def extrair_dados_agente(self, SEQ_KEY):
        query = f"""
        SELECT 
            [CHAVE SEQUENCIA] = A.GFN001,
            [ORDEM DE PRODUCAO] = A.GFDOCO,
            [SEQUENCIA REGISTRO] = A.GFN002,
            [ANALISE ML] = CASE
                WHEN GFN003 = 0 THEN 'Aprovação Requer Justificativa Plausivel da Fabrica'
                WHEN GFN003 = 1 THEN 'Ordem Não Aprovada: Limites fora da Faixa de Aceitação'
                WHEN GFN003 = 2 THEN 'Considerável Probabilidade do Analista Humano de Custos Aprovar Ordem'
                WHEN GFN003 = 3 THEN 'Ordem Não Aprovada: Limites fora da Faixa de Aceitação'
                END,
            [DECISAO DO AGENTE] = A.GFDES1,
            [JUSTIFICATIVA DO AGENTE] = A.GFNOTTE,
            [VALORES EXCEDENTES] = A.GFANSR
        FROM CRPDTA.FN31112Z A
        WHERE 
            A.GFN002 = (SELECT MAX(B.GFN002) FROM CRPDTA.FN31112Z B WHERE B.GFN001 = A.GFN001) AND
            A.GFN001 = {SEQ_KEY}
        """
        engine = self.cria_Conn()
        if engine:
            df = pd.read_sql(query, engine)
            engine.dispose()
            return df
        else:
            return None

    def get_max_sequencia(self, SEQ_KEY):
        query = f"SELECT MAX(B.GFN002) AS max_seq FROM CRPDTA.FN31112Z B WHERE B.GFN001 = {SEQ_KEY}"
        engine = self.cria_Conn()
        if engine:
            df = pd.read_sql(query, engine)
            engine.dispose()
            return df.iloc[0]['max_seq'] if not df.empty else None
        else:
            return None


@app.route('/get_variations', methods=['POST'])
def get_variations():
    data = request.json
    seq_key = data.get('seq_key')

    if not seq_key:
        return jsonify({"error": "SEQ_KEY is required"}), 400

    analise = Analise()
    data = analise.extrair_dados(seq_key)
    if data is not None:
        return data.to_json(orient="records")
    else:
        return jsonify({"error": "Error fetching data from the database"}), 500


@app.route('/get_agent_analysis', methods=['POST'])
def get_agent_analysis():
    data = request.json
    seq_key = data.get('seq_key')

    if not seq_key:
        return jsonify({"error": "SEQ_KEY is required"}), 400

    analise = Analise()
    data = analise.extrair_dados_agente(seq_key)
    if data is not None:
        return data.to_json(orient="records")
    else:
        return jsonify({"error": "Error fetching data from the database"}), 500


@app.route('/submit_justification', methods=['POST'])
def submit_justification():
    data = request.json
    seq_key = data.get('seq_key')
    justification = data.get('justification', '')

    if not seq_key:
        return jsonify({"error": "SEQ_KEY is required"}), 400

    analise = Analise()
    initial_max_seq = analise.get_max_sequencia(seq_key)

    try:
        executable_path = os.path.join(os.getcwd(), 'AI_WO_Approval.exe')
        print(f"Received justification: {justification}")
        print(f"Executing: {executable_path} {seq_key} {justification}")
        result = subprocess.run([executable_path, str(seq_key), justification], capture_output=True, text=True)
        print(f"Output: {result.stdout}")
        print(f"Error: {result.stderr}")

        final_max_seq = analise.get_max_sequencia(seq_key)
        if final_max_seq > initial_max_seq:
            return jsonify({"output": result.stdout, "error": result.stderr})
        else:
            return jsonify({
                               "error": "Ocorreu Uma Falha Na Analise. Por gentileza, clique novamente em Enviar e submeta novamente a analise aos Agentes"}), 500
    except Exception as e:
        print(f"Exception: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
