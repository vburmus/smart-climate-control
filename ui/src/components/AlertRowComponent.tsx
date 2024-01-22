import React from 'react';

const AlertRowComponent = () => {
    return (
        <tr className="border-bottom border-top-0 border-end-0 border-start-0 border-3 border-primary">
            <td className="fw-bold fs-4 text-center p-4">Call firefighters</td>
            <td className="fw-bold fs-4 text-center p-4">Smoke Detected</td>
            <td className="fw-bold fs-4 text-center p-4">101</td>
            <td className="fw-bold fs-4 text-center p-4">10.01.2024</td>
            <td className="fw-bold fs-4 text-center p-4">17:00:01</td>
        </tr>
    );
};

export default AlertRowComponent;