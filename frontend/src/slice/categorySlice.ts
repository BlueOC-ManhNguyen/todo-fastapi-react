import { createAsyncThunk, createSlice, PayloadAction } from '@reduxjs/toolkit';
import { ICategory } from '../type/category.type';
import { RootState } from '../redux/store';
import { category as data } from '../data/data';

export interface categoryState {
  status: 'idle' | 'loading' | 'succeeded' | ' failed';
  items: ICategory[];
  errors?: string;
}

const initialState: categoryState = {
  status: 'idle',
  items: data,
};

export const categorySlice = createSlice({
  name: 'category',
  initialState,
  reducers: {
    addCategory: (state, action) => {
      state.status = 'succeeded';
      let item = action.payload;
      state.items?.unshift(item);
    },
    delCategory: (state, action) => {
      state.status = 'succeeded';
      let item = action.payload;
      state.items = state.items?.filter((el) => el.id != item.id);
    },
    uptCategory: (state, action) => {
      state.status = 'succeeded';
      let updatedItem = action.payload;
      let updatedItemId = updatedItem.id;
      state.items = state.items?.map((item: ICategory) => {
        if (item.id === updatedItemId) {
          return updatedItem;
        } else {
          return item;
        }
      });
    },
  },
});

export const { addCategory, delCategory, uptCategory } = categorySlice.actions;

export const selectcategory = (state: RootState) => state.category;

export default categorySlice.reducer;
