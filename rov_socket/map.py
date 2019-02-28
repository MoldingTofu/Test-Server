def map(var, value, packet):
  path = self.topic_paths[var]
  split = path.split('.')
  p = packet
  for e in split[:-1]:
      p = p[e]
  p[split[-1]] = value


