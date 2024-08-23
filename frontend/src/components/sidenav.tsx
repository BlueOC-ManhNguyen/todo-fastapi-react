import React from "react";
import NavLinks from "./nav-links";
import UserInfo from "./userInfo";
export default function SideNav() { 
    return ( 
        <div className="flex h-full flex-col px-3 py-4 md:px-2">
        <div className="flex grow flex-row justify-between space-x-2 md:flex-col md:space-x-0 md:space-y-2">
          <div className="hidden h-auto w-full grow rounded-md bg-[#fcfaf8] md:block">
            <UserInfo/>
            <NavLinks />
          </div>
        </div>
      </div>
    )
}
