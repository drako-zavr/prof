import { api } from 'boot/axios';
import { Report } from '../models/report';

export function useReport() {
    const fetchReport = async () => {
        try {
            const { data } = await api.get<Report[]>('/content/report');
            return data;
        } catch (error) {
            console.error(error);
        }
        return [];
    };
    return {
        fetchReport
    };
}
