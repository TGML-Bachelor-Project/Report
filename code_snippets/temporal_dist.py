    # Temporal Squared Pairwise Euclidean Distance Tensor
    Dt = torch.sum(torch.square(Z.unsqueeze(0) - Z.unsqueeze(1)), dim=2)