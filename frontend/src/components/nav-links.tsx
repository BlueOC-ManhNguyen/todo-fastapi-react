import React from "react";
import {
    PlusCircleIcon,
    DocumentMagnifyingGlassIcon,
    CalendarIcon,
} from '@heroicons/react/24/outline'
import clsx from "clsx";
import { useLocation } from 'react-router-dom';

const links = [
    {
        name: "Add Task",
        icon: PlusCircleIcon,
        href: '/'
    }, 
    { 
        name: 'Search', 
        icon: DocumentMagnifyingGlassIcon,
        href: '/search'
    }, 
    { 
        name: "Upcoming", 
        icon: CalendarIcon,
        href: '/upcomming'
    }
]

export default function NavLinks () { 
    const location = useLocation()
    const pathName = location.pathname
    return ( 
        <>
           {links.map((link, index) => { 
            const LinkIcon = link.icon;
            return( 
                <a 
                    key={index}
                    href={link.href}
                    className={clsx(
                        'flex h-12 items-center justify-center gap-2 rounded-md bg-[#fcfaf8] p-3 text-sm font-medium hover:bg-[#eee] md:justify-start md:p-2 md:px-3',
                        {
                            'bg-[#ffefe5] text-[#d1453b]': pathName === link.href,
                        }
                    )}
                >
                    <LinkIcon className="w-6"/>
                    <p className="hidden md:block">{link.name}</p>
                </a>
            )
           })}
        </>
    )
}