import React from 'react';

const SummaryView = ({ results }) => {
  if (!results) return null;

  return (
    <div className="w-full max-w-4xl mx-auto space-y-6">
      {/* Summary Section */}
      <div className="bg-white rounded-lg shadow-md p-6">
        <h2 className="text-xl font-semibold text-gray-800 mb-4">Meeting Summary</h2>
        <p className="text-gray-700 leading-relaxed">{results.summary}</p>
      </div>

      {/* Key Decisions Section */}
      <div className="bg-white rounded-lg shadow-md p-6">
        <h2 className="text-xl font-semibold text-gray-800 mb-4">Key Decisions</h2>
        <ul className="space-y-2">
          {results.key_decisions && results.key_decisions.map((decision, index) => (
            <li key={index} className="flex items-start">
              <span className="text-green-500 mr-2">•</span>
              <span className="text-gray-700">{decision}</span>
            </li>
          ))}
        </ul>
      </div>

      {/* Action Items Section */}
      <div className="bg-white rounded-lg shadow-md p-6">
        <h2 className="text-xl font-semibold text-gray-800 mb-4">Action Items</h2>
        <ul className="space-y-3">
          {results.action_items && results.action_items.map((item, index) => (
            <li key={index} className="flex items-start p-3 bg-blue-50 rounded-lg">
              <span className="text-blue-500 mr-3">📌</span>
              <span className="text-gray-700">{item}</span>
            </li>
          ))}
        </ul>
      </div>

      {/* Transcript Section */}
      <div className="bg-white rounded-lg shadow-md p-6">
        <h2 className="text-xl font-semibold text-gray-800 mb-4">Full Transcript</h2>
        <div className="bg-gray-50 rounded-lg p-4">
          <p className="text-gray-700 whitespace-pre-wrap leading-relaxed">
            {results.transcript}
          </p>
        </div>
      </div>
    </div>
  );
};

export default SummaryView;