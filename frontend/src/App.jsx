import { useEffect, useState } from "react";
import { getClimateData } from "./api";

function App() {

    const [climateData, setClimateData] = useState([]);

    useEffect(() => {

        getClimateData()
            .then(response => {
                setClimateData(response.data);
            })
            .catch(error => {
                console.log(error);
            });

    }, []);

    return (
        <div>
            <h1>Climate Dashboard</h1>

            {climateData.map(data => (
                <div key={data.id}>

                    <h3>{data.region}</h3>

                    <p>
                        Temperature: {data.temperature}
                    </p>

                    <p>
                        Humidity: {data.humidity}
                    </p>

                    <p>
                        Rainfall: {data.rainfall}
                    </p>

                    <p>
                        Air Quality: {data.air_quality}
                    </p>

                    <p>
                        Date: {data.recorded_date}
                    </p>

                </div>
            ))}
        </div>
    );
}

export default App;
