import dayjs from 'dayjs';

export interface ICategory {
  id: number;
  userId: number;
  name: string;
  createdAt: dayjs.Dayjs;
  updatedAt: dayjs.Dayjs;
}
