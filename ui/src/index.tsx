import React from 'react';
import {BrowserRouter as Router} from "react-router-dom";
import {createRoot} from 'react-dom/client';
import App from './App';
import 'bootstrap/dist/css/bootstrap.css';

const root = document.getElementById('root') as HTMLElement

const rootReact = createRoot(root);
rootReact.render(
    <Router>
        <App/>
    </Router>
);