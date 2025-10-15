import React, { useState } from 'react';
import { uploadAudio } from '../api';

const UploadAudio = ({ onResults }) => {
  const [isUploading, setIsUploading] = useState(false);
  const [error, setError] = useState('');

  const handleFileUpload = async (event) => {
    const file = event.target.files[0];
    if (!file) return;

    // Validate file type
    const validTypes = ['audio/mp3', 'audio/wav', 'audio/mpeg', 'audio/x-m4a'];
    if (!validTypes.includes(file.type)) {
      setError('Please upload an MP3, WAV, or M4A file');
      return;
    }

    // Validate file size (max 50MB)
    if (file.size > 50 * 1024 * 1024) {
      setError('File size must be less than 50MB');
      return;
    }

    setIsUploading(true);
    setError('');

    try {
      const results = await uploadAudio(file);
      onResults(results);
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to upload and process audio');
      console.error('Upload error:', err);
    } finally {
      setIsUploading(false);
    }
  };

  return (
    <div className="w-full max-w-md mx-auto">
      <div className="border-2 border-dashed border-gray-300 rounded-lg p-6 text-center">
        <input
          type="file"
          accept=".mp3,.wav,.m4a,audio/*"
          onChange={handleFileUpload}
          disabled={isUploading}
          className="hidden"
          id="audio-upload"
        />
        <label
          htmlFor="audio-upload"
          className={`cursor-pointer block ${
            isUploading ? 'opacity-50 cursor-not-allowed' : ''
          }`}
        >
          <div className="flex flex-col items-center justify-center">
            <svg
              className="w-12 h-12 text-gray-400 mb-3"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 48 48"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02"
              />
            </svg>
            <span className="text-lg font-medium text-gray-700">
              {isUploading ? 'Processing...' : 'Upload Meeting Audio'}
            </span>
            <p className="text-sm text-gray-500 mt-1">
              MP3, WAV, or M4A files up to 50MB
            </p>
          </div>
        </label>
      </div>
      
      {error && (
        <div className="mt-3 p-3 bg-red-50 border border-red-200 rounded-md">
          <p className="text-sm text-red-600">{error}</p>
        </div>
      )}
      
      {isUploading && (
        <div className="mt-3">
          <div className="flex items-center justify-center space-x-2">
            <div className="w-4 h-4 bg-blue-500 rounded-full animate-bounce"></div>
            <div className="w-4 h-4 bg-blue-500 rounded-full animate-bounce" style={{ animationDelay: '0.1s' }}></div>
            <div className="w-4 h-4 bg-blue-500 rounded-full animate-bounce" style={{ animationDelay: '0.2s' }}></div>
          </div>
          <p className="text-center text-sm text-gray-600 mt-2">
            Processing audio... This may take a minute.
          </p>
        </div>
      )}
    </div>
  );
};

export default UploadAudio;