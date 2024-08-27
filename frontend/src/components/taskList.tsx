import React, { useState } from 'react';
import { ICategory } from '../type/category.type';

interface CategoryList {
  data: ICategory[];
}

export default function TaskList({ data }: CategoryList) {
  return (
    <>
      {data &&
        data.map((item, index) => {
          const { id, userId, name, createdAt, updatedAt } = item;
          return (
            <button
              key={index}
              className="flex h-12 w-full items-center justify-center gap-2 rounded-md bg-[#fcfaf8] p-3 text-sm font-medium hover:bg-[#eee] md:justify-start md:p-2 md:px-3"
            >
              <p className="hidden md:block ">{name}</p>
            </button>
          );
        })}
    </>
  );
}
