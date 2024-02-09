import axios from 'axios';

const axiosInstance = axios.create({
    baseURL: 'https://156.17.234.83:8080'
})

export default axiosInstance;