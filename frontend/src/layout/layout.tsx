import React from 'react';
import { Outlet, useNavigate } from 'react-router-dom';

export default function Layout({ children }: { children?: React.ReactNode }) {
  return (
    <div className="flex h-screen flex-col md:flex-row md:overflow-hidden">
      <Outlet />
    </div>
  );
}
