import React, { useState } from 'react';
import UploadAudio from './components/UploadAudio';
import SummaryView from './components/SummaryView';

function App() {
  const [results, setResults] = useState(null);

  const handleResults = (data) => {
    setResults(data);
  };

  const resetResults = () => {
    setResults(null);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 py-8">
      <div className="container mx-auto px-4">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-800 mb-2">
            Meeting Summarizer
          </h1>
          <p className="text-lg text-gray-600">
            Upload meeting audio and get instant transcripts, summaries, and action items
          </p>
        </div>

        {/* Upload Section */}
        {!results ? (
          <UploadAudio onResults={handleResults} />
        ) : (
          <div className="space-y-6">
            <div className="text-center">
              <button
                onClick={resetResults}
                className="bg-blue-500 hover:bg-blue-600 text-white font-medium py-2 px-6 rounded-lg transition duration-200"
              >
                Analyze Another Meeting
              </button>
            </div>
            <SummaryView results={results} />
          </div>
        )}

        {/* Footer */}
        <div className="text-center mt-12">
          <p className="text-sm text-gray-500">
            Powered by Grok AI • Audio processing may take a few moments
          </p>
        </div>
      </div>
    </div>
  );
}

export default App;