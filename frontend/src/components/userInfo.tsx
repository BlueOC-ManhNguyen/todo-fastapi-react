import React from "react";
import {
    UserCircleIcon
} from '@heroicons/react/24/outline'

export default function UserInfo() { 
    return ( 
        <div
            className="flex h-12 items-center justify-center gap-2 rounded-md bg-[#fcfaf8] p-3 text-sm font-medium hover:bg-[#eee] md:justify-start md:p-2 md:px-3">
                <UserCircleIcon className ="w-6"/>
                <p className="hidden md:block">Hieu Ngo</p>
        </div>
    )
}