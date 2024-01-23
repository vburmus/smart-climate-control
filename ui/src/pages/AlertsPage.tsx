import React, {useEffect, useState} from 'react';
import Loader from "../components/common/Loader";
import AlertRowComponent from "../components/AlertRowComponent";
import {isAxiosError} from "axios";
import {Alert} from "../utils/types";
import {findAllAlerts} from "../utils/alertsUtils";
const AlertsPage = () => {
    const alertParams = [
        "Action", "Cause", "Room", "Date", "Time"
    ];
    const [isLoading, setIsLoading] = useState(false)
    const [alerts, setAlerts] = useState<Alert[]>()
    const [error, setError] = useState()


    const fetchData = async () => {
        try {
            const result = await findAllAlerts();
            setAlerts(result.alerts)
        } catch(e) {
            if (isAxiosError(e) && e.response) {
                setError(e.response.data.message)
            }
        } finally {
            setIsLoading(false);
        }
    };

    useEffect(() => {
        fetchData()
    }, []);

    return (isLoading ? <Loader/> : error || !alerts ? <h1 className="m-5 fw-bold text-center text-danger">{error}</h1> :
            <div className="d-flex flex-column m-5 gap-3 w-75">
                <h1 className="fw-bold text-primary text-center">Your alerts:</h1>

                <table style={{ borderRadius: '20px', overflow: 'hidden' }}>
                    <thead className="bg-primary">
                        <tr className="border-bottom border-top-0 border-end-0 border-start-0 border-3 border-primary">
                            {alertParams.map((cat) => {
                                return <th className="fw-bold text-white fs-3 text-center rounded-top-3 p-3">{cat}</th>
                            })}
                        </tr>
                    </thead>
                    <tbody>
                    {alerts.map((alert) => {
                        return <AlertRowComponent alert={alert}/>
                    })}
                    </tbody>

                </table>
            </div>
    );
};

export default AlertsPage;