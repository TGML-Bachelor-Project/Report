    #Non-Event Intensity Vectorized Summation
    # Summing node pair intensities over steps
    node_pair_intensities = torch.sum(stepwise_node_pair_intensities,dim=2)
    # Summing upper triangular node pair intensities due to symmetry
    In = torch.sum(node_pair_intensities.triu(diagonal=1))