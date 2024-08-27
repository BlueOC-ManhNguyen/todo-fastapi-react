import React from 'react';
import logo from './logo.svg';
import './App.css';
import Layout from './layout/layout';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Provider } from 'react-redux';
import { store } from './redux/store';

import Home from './page/homepage';
import AddTask from './page/add-task';
import Search from './page/search';
import UpComming from './page/up-comming';

function App() {
  return (
    <Provider store={store}>
      <Router>
        <Routes>
          {/* <Route element = {<Layout/>}>
          <Route path='/' element={<AddTask />}/>
          <Route path='/search' element={<Search />}/>
          <Route path='/upcomming' element={<UpComming />}/>
        </Route> */}
          <Route element={<Layout />}>
            <Route path="/" element={<Home />} />
          </Route>
        </Routes>
      </Router>
    </Provider>
  );
}

export default App;
