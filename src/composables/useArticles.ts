import { api } from 'boot/axios';
import { Article } from '../models/article';

export function useArticles() {
    const fetchArticles = async () => {
        try {
            const { data } = await api.get<Article[]>('/articles/list');
            return data;
        } catch (error) {
            console.error(error);
        }
        return [];
    };
    return {
        fetchArticles
    };
}
