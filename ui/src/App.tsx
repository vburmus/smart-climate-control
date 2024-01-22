import React from 'react';
import './styles/App.css';
import Header from "./components/common/Header";
import {Route, Routes} from "react-router-dom";
import HomePage from "./pages/HomePage";
import RoomsPage from "./pages/RoomsPage";
import AlertsPage from "./pages/AlertsPage";


function App() {
  return (
    <main>
        <Header/>
        <Routes>
            <Route path="/" element={<HomePage/>}/>
            <Route path="/rooms" element={<RoomsPage/>}/>
            <Route path="/alerts" element={<AlertsPage/>}/>
        </Routes>
    </main>
  );
}

export default App;
