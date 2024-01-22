import React from 'react';
import "../../styles/Loader.css"

const Loader = () => {
    return (
        <div className="loader">
            <div className="spinner-border text-primary" role="status">
                <span className="sr-only"></span>
            </div>
        </div>
    );
};

export default Loader;