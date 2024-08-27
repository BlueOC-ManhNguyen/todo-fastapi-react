import React, { useState, useEffect } from 'react';
import dayjs from 'dayjs';
import Layout from '../../layout/layout';
import NavLinks from '../../components/navLinks';
import UserInfo from '../../components/userInfo';
import Modal from '../../components/modal';
import TaskList from '../../components/taskList';

import { useAppDispatch, useAppSelector } from '../../redux/store';
import { addCategory } from '../../slice/categorySlice';
import { ICategory } from '../../type/category.type';

export default function Home() {
  const now = dayjs();

  const [isModalOpen, setIsModalOpen] = useState(false);
  const [categoryName, setCategoryName] = useState('');
  const [data, setData] = useState<ICategory[]>([]);
  const dispatch = useAppDispatch();
  const category = useAppSelector((state) => state.category);
  const { status, items } = category;
  useEffect(() => {
    setData(category.items);
  }, [items]);

  const handleButtonClick = () => {
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
  };

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (categoryName.trim() === '') {
      console.log('Category name cannot be empty');
      return;
    }
    const valueSubmit = {
      id: Date.now(), // Sử dụng timestamp để tạo id duy nhất
      userId: 1, // Thay đổi thành ID người dùng thực tế nếu cần
      name: categoryName,
      createdAt: now.unix(),
      updatedAt: now.unix(),
    };
    dispatch(addCategory(valueSubmit));
    closeModal();
    setCategoryName('');
  };

  return (
    <>
      <div className="w-full flex-none md:w-64">
        <div className="flex h-full flex-col px-3 py-4 md:px-2">
          <div className="flex grow flex-row justify-between space-x-2 md:flex-col md:space-x-0 md:space-y-2">
            <div className="hidden h-auto w-full grow rounded-md bg-[#fcfaf8] md:block">
              <UserInfo />
              <NavLinks onModal={handleButtonClick} />
              <TaskList data={data} />
            </div>
          </div>
        </div>
      </div>
      <div className="grow p-6 md:overflow-y-auto md:p-12"></div>
      <Modal open={isModalOpen} title="Add Category" close={closeModal}>
        <form className="space-y-4" onSubmit={handleSubmit}>
          <div>
            <label
              htmlFor="name"
              className="block text-sm font-medium text-gray-700 mb-1"
            >
              Category Name:
            </label>
            <input
              type="text"
              id="name"
              name="name"
              autoFocus
              value={categoryName}
              onChange={(e) => setCategoryName(e.target.value)}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            />
          </div>
          <button
            type="submit"
            className="mt-6 w-full px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50"
          >
            Submit
          </button>
        </form>
      </Modal>
    </>
  );
}
