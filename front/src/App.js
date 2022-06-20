import logo from './logo.svg';
import './App.css';
import Nav from './Components/Nav';
import MainPage from './Components/MainPage';
import Footer from './Components/Footer';
import React, {Component} from 'react';
import {BrowserRouter,
  Routes,
  Route,
  Link
} from "react-router-dom";

class App extends Component {
  render(){
  return (
    <div>

      <MainPage/>
      <Footer/>
    </div>
  );
  }
}

export default App;
