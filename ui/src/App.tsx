import React from 'react';
import './styles/App.css';
import Header from "./components/common/Header";
import {Route, Routes} from "react-router-dom";
import HomePage from "./pages/HomePage";
import RoomsPage from "./pages/RoomsPage";
import AlertsPage from "./pages/AlertsPage";
import RoomDetailsPage from "./pages/RoomDetailsPage";


function App() {
  return (
    <main>
        <Header/>
        <div className="page">
            <Routes>
                <Route path="/" element={<HomePage/>}/>
                <Route path="/rooms" element={<RoomsPage/>}/>
                <Route path="/alerts" element={<AlertsPage/>}/>
                <Route path="/room/:id" element={<RoomDetailsPage/>}/>
            </Routes>
        </div>
    </main>
  );
}

export default App;
