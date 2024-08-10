# Social Function Of Domestic Facial Signals
The repository for the paper "Computational Investigation of the Social Function of Domestic Cat Facial Signals".

## Abstract
There is growing interest in the facial signals of domestic cats. Domestication may have shifted feline social dynamics towards a greater emphasis on facial signals that promote affiliative bonding.  Most studies have focused on cat facial signals during human interactions or in response to pain.  Research on intraspecific facial communication in cats has predominantly examined non-affiliative social interactions. A recent study by Scott and Florkiewicz (2023) demonstrated significant differences between cats' facial signals during affiliative and non-affiliative intraspecific interactions. This follow-up study applies computational approaches to make two main contributions. First, we develop a machine learning classifier for affiliative/non-affiliative interactions based on manual CatFACS codings and automatically detected facial landmarks, reaching above 77\% in CatFACS codings and 68\% in landmarks by integrating a temporal dimension. Secondly, we introduce novel measures for rapid facial mimicry based on CatFACS coding. Our analysis suggests that domestic cats exhibit more rapid facial mimicry in affiliative contexts than non-affiliative ones, which is consistent with the proposed function of mimicry. Moreover, we found that ear movements (such as EAD103 and EAD104) are highly prone to rapid facial mimicry. Our research introduces new possibilities for analyzing cat facial signals and exploring shared moods with innovative AI-based approaches.

## Features

- **CatFACS-Based Approach**: Analyzes manually coded CatFACS variables and compares non-temporal (random) and temporal (ordered) data.
- **Facial Landmarks-Based Approach**: Processes raw video data to extract facial landmarks and analyze interactions between cats.
- **Rapid Facial Mimicry Metrics**: Implements metrics like RMsize and RMratio to quantify mimicry in cat facial expressions.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/catfacs-rapid-mimicry.git
   cd catfacs-rapid-mimicry```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage
1. Prepare data - Ensure that your data is formatted correctly as sequences of CatFACS variables or facial landmarks with timestamps.
2. Calculate Metrics - Use the provided Python functions to calculate the RMsize and RMratio metrics for your data.
3. Analyze results - Interpret the results from the RMsize and RMratio metrics to understand the level of rapid facial mimicry in your data

## How to cite
If you use this code or find it helpful in your research, please cite our work as follows:
```
@article{martvel2024catfacs,
  title={Computational Investigation of the Social Function of Domestic Cat Facial Signals},
  author={Marvel, G. and Scott, L. and Florkiewicz, B. and Zamansky, A. and Shimshoni, I. and Lazebnik, T.},
  year={2024},
  jornal = {TBD}
}
```

## Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss your changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Data
The data is avalible upon reasinable request from the corosponding author.
