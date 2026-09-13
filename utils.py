import numpy as np


def multi_evaluation(simi, mask, targets_, args):
    """
    simi: shape: [n, num_class], the similarity between visual features and all num_class semantic labels;
    mask: shape: [n_class, num_nodes], each row indicates the label is composed of which attributes and objects;
    targets: shape: [n, 1], ground truth, range form 0 to num_class-1;
    """

    scores_ = mask[np.argmax(simi, axis=1)]
    targets_ = mask[np.squeeze(targets_)]

    n_sample, n_class = scores_.shape
    nc_attr_hard, nc_attr_soft = np.zeros(n_sample), np.zeros(n_sample)
    nc_obj = np.zeros(n_sample)
    for k in range(n_sample):
        pos_count_hard = 0
        pos_count_soft = 0
        total_count = 0
        calibration_factor = 1.0
        pred, gt = scores_[k, :args.num_attrs], targets_[k, :args.num_attrs]
        pred_idx, gt_idx = np.where(pred == 1)[0], np.where(gt == 1)[0]  # e.g., [ 93  97 115] [ 78  97 115]
        com = [list(combinations(gt_idx, i+1)) for i in range(len(gt_idx))]  # e.g., [[(78,), (97,), (115,)], [(78, 97), (78, 115), (97, 115)], [(78, 97, 115)]]
        com = list(itertools.chain.from_iterable(com))  # e.g., [(78,), (97,), (115,), (78, 97), (78, 115), (97, 115), (78, 97, 115)]

        n_com = len(com)
        for j in range(n_com):
            if set(com[j]).issubset(set(pred_idx)):
                pos_count_hard += 1
            if not set(com[j]).isdisjoint(set(pred_idx)):
                pos_count_soft += 1
            if len(pred_idx) > len(gt_idx):
                calibration_factor = 1 / 1.1 ** (len(pred_idx) - len(gt_idx))
            total_count += 1
        nc_attr_hard[k] = pos_count_hard / total_count * calibration_factor
        nc_attr_soft[k] = pos_count_soft / total_count * calibration_factor
        nc_obj[k] = ((scores_[k, args.num_attrs:] - targets_[k, args.num_attrs:]) ** 2).sum() == 0

    # print(nc_attr_hard.mean())
    # print(nc_attr_soft.mean())
    # print(nc_obj.mean())

    return (nc_attr_hard * nc_obj).mean(), (nc_attr_soft * nc_obj).mean()