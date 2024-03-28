export interface Article {
    readonly id: number;
    title: string;
    photo: string | null;
    content: string;
    images: ImagesModel[];

  }
export interface ImagesModel {
    readonly id: number;
    photo: string | null;
    order: number;
}