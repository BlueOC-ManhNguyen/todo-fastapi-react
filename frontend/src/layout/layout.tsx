import React from "react";
import SideNav from "../components/sidenav";
import { Outlet } from "react-router-dom"

export default function Layout({ children }: { children?: React.ReactNode }) {
    return (
      <div className="flex h-screen flex-col md:flex-row md:overflow-hidden">
        <div className="w-full flex-none md:w-64">
          <SideNav />
        </div>
        <div className="grow p-6 md:overflow-y-auto md:p-12">
            <Outlet/>
        </div>
      </div>
    );
  }
  