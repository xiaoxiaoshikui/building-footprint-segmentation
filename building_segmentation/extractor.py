from typing import List

import torch


class Extractor:
    def __init__(self, segmentation):
        self.segmentation = segmentation

    def load_model(self, model_name, **model_param):
        return self.segmentation.create_network(model_name, **model_param)

    def load_criterion(self, criterion_name, **criterion_param):
        return self.segmentation.create_criterion(criterion_name, **criterion_param)

    def load_loader(
        self, root_folder, image_normalization, label_normalization, batch_size
    ):
        return self.segmentation.create_loader(
            root_folder, image_normalization, label_normalization, batch_size
        )

    def load_metrics(self, data_metrics: List[str]):
        return self.segmentation.create_metrics(data_metrics)

    @staticmethod
    def load_optimizer(model, optimizer_name, **optimizer_param):
        return getattr(torch.optim, optimizer_name)(
            filter(lambda p: p.requires_grad, model.parameters()), **optimizer_param
        )


def init_extractor(segmentation_type: str):
    if segmentation_type == "binary":
        from building_segmentation.ml.binary.factory import BinaryFactory

        return Extractor(BinaryFactory())
    else:
        raise NotImplementedError
