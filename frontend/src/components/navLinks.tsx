import React, { useState } from "react";
import {
    PlusCircleIcon,
    DocumentMagnifyingGlassIcon,
    CalendarIcon,
} from '@heroicons/react/24/outline';

interface NavProps {
    onModal: () => void;
}

export default function NavLinks({ onModal }: NavProps) {

    return (
        <>
            <button
                className='flex h-12 w-full items-center justify-center gap-2 rounded-md bg-[#fcfaf8] p-3 text-sm font-medium hover:bg-[#eee] md:justify-start md:p-2 md:px-3'
                onClick={onModal}
            >
                <PlusCircleIcon className="w-6" />
                <p className="hidden md:block">Add Category</p>
            </button>
        </>
    );
}
