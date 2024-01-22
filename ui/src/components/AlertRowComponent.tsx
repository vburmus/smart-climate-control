import React from 'react';
import {Alert} from "../utils/types";

type AlertRowProps = {
    alert: Alert
}

const AlertRowComponent = ({alert}: AlertRowProps) => {
    return (
        <tr className="border-bottom border-top-0 border-end-0 border-start-0 border-3 border-primary">
            <td className="fw-bold fs-4 text-center p-4">{alert.action}</td>
            <td className="fw-bold fs-4 text-center p-4">{alert.cause}</td>
            <td className="fw-bold fs-4 text-center p-4">{alert.id}</td>
            <td className="fw-bold fs-4 text-center p-4">{alert.date.substring(0, 10)}</td>
            <td className="fw-bold fs-4 text-center p-4">{alert.date.substring(10,19)}</td>
        </tr>
    );
};

export default AlertRowComponent;