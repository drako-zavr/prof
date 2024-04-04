export interface Article {
    readonly id: number;
    title: string;
    photo: string | null;
    content: string;
    images: ImagesModel[];
    documents: DocumentsModel[];

  }
export interface ImagesModel {
    readonly id: number;
    photo: string | null;
    order: number;
}
export interface DocumentsModel {
  readonly id: number;
  title: string;
  fileContent: string;
}