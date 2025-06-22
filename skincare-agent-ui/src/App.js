import React, { useState } from 'react';
import './App.css';

function App() {
    const [query, setQuery] = useState('');
    const [response, setResponse] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);


    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError(null);
        setResponse('');

        try {
            const res = await fetch('http://localhost:5000/ask', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ query })
            });
            const data = await res.json();
            if(data.error) {
                setError(data.error);
            } else {
                setResponse(data.response);
            }
        } catch (err) {
            setError('Server error: ' + err.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className= {`container ${response ? 'shrink' : 'hero' }`}>
            <h1> Skinwise </h1>
            <h2> Your Smart Agentic AI Skincare Assistant </h2>
            <form onSubmit={handleSubmit}>
                <input
                type='text'
                placeholder='Ask a skincare question...'
                value = {query}
                onChange={(e) => setQuery(e.target.value)}
                />
                <button type='submit' disabled={loading || !query.trim()}>
                    {loading ? 'Thinking..' : 'Ask'}
                </button>
            </form>
            {error && <div className='error'> {error} </div>}
            {response && (
                <div className="response">
                  <h3>✅ Response:</h3>
                  <div dangerouslySetInnerHTML={{ __html: response }} />
                </div>
            )}
        </div>
    );
}

export default App;