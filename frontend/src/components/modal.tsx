import React from 'react';

interface ModalProps {
  open?: boolean;
  title?: string;
  children?: React.ReactNode;
  close?: () => void;
}

const Modal: React.FC<ModalProps> = ({ open, title, children, close }) => {
  return (
    <>
    {open && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50">
        <div className="bg-white p-6 rounded-md shadow-lg w-full max-w-sm">
          <h2 className="text-lg font-medium mb-4">{title}</h2>
              {children}
          <button
            onClick={close}
            className="mt-1 w-full px-4 py-2 bg-red-500 text-white rounded-md hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-opacity-50"
          >
            Close
          </button>
        </div>
      </div>
    )}
    </>
  );

};

export default Modal;
