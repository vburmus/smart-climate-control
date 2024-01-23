import React from 'react';
import {Button, Image} from "react-bootstrap";
import "../../styles/Header.css"
import {Link, useLocation} from "react-router-dom";
import logoImage from "../../assets/images/logo.png"

const Header = () => {
    const location = useLocation()

    const routes = [
        { path: '/', label: 'Home' },
        { path: '/rooms', label: 'Rooms' },
        { path: '/alerts', label: 'Alerts' },
    ];

    const getLinkClass = (path: string) =>
        `fw-bold ${location.pathname === path ? 'text-info border-bottom border-2 border-info' : ''}`;

    return (
        <header className="navbar text-primary shadow-lg d-flex p-4 px-5 justify-content-between">
            <Link to="/">
                <Image src={logoImage} className="img-fluid logo"/>
            </Link>
            <div className="d-flex gap-5">
                {routes.map((route) => (
                    <Link key={route.path} to={route.path} style={{ textDecoration: 'none' }}>
                        <h3 className={getLinkClass(route.path)}>{route.label}</h3>
                    </Link>
                ))}
            </div>
            <Link to="/">
                <Button variant="primary" className="rounded-3 fw-bold text-white fs-5">
                    About Us
                </Button>
            </Link>
        </header>
    );
};

export default Header;