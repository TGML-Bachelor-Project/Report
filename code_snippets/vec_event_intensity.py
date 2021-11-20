    # Vectorized computation of event intensities
    Ie = torch.sum(log_intensities[i,j,unique_time_indices])