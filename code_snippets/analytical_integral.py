    # Vectorizing variables for Analytical Integral of Non-event Intensity
    a = (z0[:,0].unsqueeze(1) - z0[:,0].unsqueeze(0)) + torch.eps
    b = (z0[:,1].unsqueeze(1) - z0[:,1].unsqueeze(0)) + torch.eps
    m = (v0[:,0].unsqueeze(1) - v0[:,0].unsqueeze(0)) + torch.eps
    n = (v0[:,1].unsqueeze(1) - v0[:,1].unsqueeze(0)) + torch.eps