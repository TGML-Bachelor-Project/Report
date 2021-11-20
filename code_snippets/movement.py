    # Calculating movements in time for each node
    movement = torch.sum(self.V.unsqueeze(2)*time_deltas, dim=3)