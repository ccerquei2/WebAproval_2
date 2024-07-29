import React, { useState } from 'react';
import './App.css';  // Adicione esta linha para importar o CSS

function App() {
  const [seqKey, setSeqKey] = useState('');
  const [justification, setJustification] = useState('');
  const [variations, setVariations] = useState(null);
  const [agentAnalysis, setAgentAnalysis] = useState(null);
  const [exceededValues, setExceededValues] = useState(null);
  const [message, setMessage] = useState('');

  const fetchVariations = async () => {
    setMessage('');
    try {
      const res = await fetch('http://127.0.0.1:5000/get_variations', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ seq_key: seqKey })
      });
      if (!res.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await res.json();
      setVariations(data);
      fetchAgentAnalysis();
    } catch (error) {
      console.error('Failed to fetch:', error);
      setMessage('Failed to fetch variations.');
    }
  };

  const fetchAgentAnalysis = async () => {
    try {
      const res = await fetch('http://127.0.0.1:5000/get_agent_analysis', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ seq_key: seqKey })
      });
      if (!res.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await res.json();
      setAgentAnalysis(data[0]);

      if (data[0] && data[0]['ANALISE ML'] === 'Ordem Não Aprovada: Limites fora da Faixa de Aceitação') {
        const exceededValues = JSON.parse(data[0]['VALORES EXCEDENTES'])[0];
        setExceededValues(exceededValues);
      } else {
        setExceededValues(null);
      }
    } catch (error) {
      console.error('Failed to fetch agent analysis:', error);
      setMessage('Failed to fetch agent analysis.');
    }
  };

  const submitJustification = async () => {
    setMessage('');
    setAgentAnalysis(null);  // Limpar o quadro "Analise do Agente"
    setExceededValues(null);  // Limpar o quadro "Analise Valores Excedentes"
    try {
      const res = await fetch('http://127.0.0.1:5000/submit_justification', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ seq_key: seqKey, justification })
      });
      const data = await res.json();
      if (res.ok) {
        console.log(data);
        setMessage('Justification submitted successfully.');
        fetchVariations();  // Chamar automaticamente a função fetchVariations após a execução do .exe
      } else {
        setMessage(data.error);
      }
    } catch (error) {
      console.error('Failed to fetch:', error);
      setMessage('Failed to submit justification.');
    }
  };

  const formatNumber = (num) => {
    return num ? num.toFixed(2) : '0.00';
  };

  return (
    <div className="container">
      <img src="/LogoGranado.jpg" alt="Granado AI Solution" className="logo" />
      <h1>Analise e Aprovação de WO por Agentes IA</h1>
      <form onSubmit={(e) => e.preventDefault()}>
        <label className="variaçoes">Variações</label>
        <input 
          type="text" 
          value={seqKey} 
          onChange={(e) => setSeqKey(e.target.value)} 
          placeholder="SEQ_KEY"
        />
        <button type="button" onClick={fetchVariations}>Carregar</button>
      </form>
      {variations && (
        <div>
          <table>
            <thead>
              <tr>
                <th>SEQ_KEY</th>
                <th>ORDEM</th>
                <th>VARIACAO_IMXIC</th>
                <th>DIF_CUSTO_P_x_R</th>
                <th>MAT_DIF_PERCENTUAL</th>
                <th>TAXA_MAQUINA_FIXA</th>
                <th>TAXA_MO_FIXA</th>
                <th>TAXA_FIXA_VAR_MO</th>
                <th>MO_VALOR</th>
                <th>HR_MAQ_VALOR</th>
                <th>HR_EXC_VLR</th>
                <th>HR_CONFIG_VLR</th>
                <th>MO_VARIACAO</th>
                <th>EXTERNA_OPERACAO</th>
              </tr>
            </thead>
            <tbody>
              {variations.map((row, index) => (
                <tr key={index}>
                  {Object.values(row).map((cell, cellIndex) => (
                    <td key={cellIndex} style={{ backgroundColor: cellIndex === 2 && cell < 0 ? 'green' : 'white' }}>
                      {cell}
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
      <div>
        <h2>Justificativa</h2>
        <textarea 
          value={justification} 
          onChange={(e) => setJustification(e.target.value)} 
          placeholder="Justificativa Fabrica"
          className="agent-justification"
        />
        <button type="button" onClick={submitJustification}>Enviar</button>
      </div>
      {agentAnalysis && (
        <div>
          <h2>Analise do Agente</h2>
          <table style={{ width: '100%' }}>
            <tbody>
              <tr>
                <td>CHAVE SEQUENCIA</td>
                <td>{agentAnalysis['CHAVE SEQUENCIA']}</td>
              </tr>
              <tr>
                <td>ORDEM DE PRODUCAO</td>
                <td>{agentAnalysis['ORDEM DE PRODUCAO']}</td>
              </tr>
              <tr>
                <td>SEQUENCIA REGISTRO</td>
                <td>{agentAnalysis['SEQUENCIA REGISTRO']}</td>
              </tr>
              <tr>
                <td>ANALISE ML</td>
                <td>{agentAnalysis['ANALISE ML']}</td>
              </tr>
              <tr>
                <td>DECISAO DO AGENTE</td>
                <td>{agentAnalysis['DECISAO DO AGENTE']}</td>
              </tr>
              <tr>
                <td>JUSTIFICATIVA DO AGENTE</td>
                <td>
                  <textarea 
                    value={agentAnalysis['JUSTIFICATIVA DO AGENTE']} 
                    readOnly 
                    className="agent-justification" 
                  />
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      )}
      {exceededValues && (
        <div>
          <h2>Analise Valores Excedentes</h2>
          <table>
            <thead>
              <tr>
                <th>Campo</th>
                <th>Valor</th>
                <th>Limite</th>
              </tr>
            </thead>
            <tbody>
              {Object.keys(exceededValues).map((key, index) => {
                if (key.endsWith('_EXCEDE_LIMITE') && exceededValues[key]) {
                  const valueKey = key.replace('_EXCEDE_LIMITE', '');
                  return (
                    <tr key={index}>
                      <td>{valueKey}</td>
                      <td>{formatNumber(exceededValues[valueKey])}</td>
                      <td>{formatNumber(exceededValues[`LIMITE_${valueKey}`])}</td>
                    </tr>
                  );
                }
                return null;
              })}
            </tbody>
          </table>
        </div>
      )}
      {message && <p style={{ color: 'red', fontWeight: 'bold' }}>{message}</p>}
    </div>
  );
}

export default App;
