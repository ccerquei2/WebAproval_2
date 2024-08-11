import React, { useState } from 'react';
import './App.css';

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
    setAgentAnalysis(null);
    setExceededValues(null);
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
        fetchVariations();
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
      <h1>Aprovação de WO Assistida por AI</h1>
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
                <th>SEQ KEY</th>
                <th>ORDEM</th>
                <th>VARIACAO IM X IC</th>
                <th>CUSTO REAL X PADRAO</th>
                <th>DIF MATERIAL</th>
                <th>TAXA MAQUINA FIXA</th>
                <th>TAXA MO FIXA</th>
                <th>TAXA VAR MO</th>
                <th>MO VALOR</th>
                <th>HR MAQ VALOR</th>
                <th>HR EXC VLR</th>
                <th>HR CONFIG VLR</th>
                <th>MO VARIACAO</th>
                <th>EXTERNA OPERACAO</th>
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
        <div className="agent-analysis-container">
          <h2>Analise do Agente</h2>
          <table className="table-agent-analysis">
            <tbody>
              <tr>
                <td className="label-cell">CHAVE SEQUENCIA</td>
                <td>{agentAnalysis['CHAVE SEQUENCIA']}</td>
              </tr>
              <tr>
                <td className="label-cell">ORDEM DE PRODUCAO</td>
                <td>{agentAnalysis['ORDEM DE PRODUCAO']}</td>
              </tr>
              <tr>
                <td className="label-cell">SEQUENCIA REGISTRO</td>
                <td>{agentAnalysis['SEQUENCIA REGISTRO']}</td>
              </tr>
              <tr>
                <td className="label-cell">ANALISE ML</td>
                <td>{agentAnalysis['ANALISE ML']}</td>
              </tr>
              <tr>
                <td className="label-cell">DECISAO DO AGENTE</td>
                <td>{agentAnalysis['DECISAO DO AGENTE']}</td>
              </tr>
              <tr>
                <td className="label-cell">JUSTIFICATIVA DO AGENTE</td>
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
                <th>Dado</th>
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
