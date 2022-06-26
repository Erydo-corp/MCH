import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import Register from './Components/Register'
import reportWebVitals from './reportWebVitals';
import { BrowserRouter, Routes,
  Route,
  Link} from "react-router-dom";
import VacansList from './Components/VacasList';
import Nav from './Components/Nav';
import OneVac from './Components/OneVac';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <BrowserRouter>
    <Nav/>
    <Routes>
      <Route path="/" element={<App />} />
      <Route path='register' element={<Register/>}/>
      <Route path='vacansi' element={<VacansList/>}/>
      <Route path='diskription-vacansy' element={<OneVac/>}/>
    </Routes>
    </BrowserRouter>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
