import { api } from 'boot/axios';
import { Memory } from '../models/memory';

export function useMemory() {
    const fetchMemory = async () => {
        try {
            const { data } = await api.get<Memory[]>('/content/memory');
            return data;
        } catch (error) {
            console.error(error);
        }
        return [];
    };
    return {
        fetchMemory
    };
}
