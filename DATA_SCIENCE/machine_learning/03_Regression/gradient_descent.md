# 확률적 경사 하강법 (Statistical Gradient Descent)
> 에러를 최소화 하기 위한 방안이다. (손실을 줄이는 알고리즘)
> 랜덤하게 샘플을 선택하고 기울기를 조정하며 최저점을 찾는 방안이다.
> ![](https://images.velog.io/images/arittung/post/c042f965-cbc2-4ab7-9e60-3194ed2038b0/image.png)
> 기울기가 음의 기울기이면 우로 이동, 양의 기울기이면 좌로 이동
> 기울기에 대한 오차를 기울기를 조정하며 모두 체크했을 때 2차 함수꼴로 나타난다.
>
> **에포크**: 훈련세트를 다 사용했지만 최저점에 도달하지 못했을 때 모든 훈련세트를 다시 복구시키고 처음부터 다시 시작해서 만족할만한 지점에 도달할 때까지 반복할 때, 한 번의 반복을 에포크라고 한다.
>
> - **손실함수**: 예측값과 실제값의 오차를 기하는 기준으로 샘플 하나에 대한 손실
> - **비용함수**: 모든 샘플에 대한 손실 함수의 합

## 확률적 경사 하강법
1. 학습, 테스트 데이터 나누기
2. `from sklearn.preprocessing import StandardScaler`: 학습 데이터에 학습시켜서 스케일의 크기 조정을 한다.
   - 변수들의 스케일이 너무 다를 경우 크기 조정을 위해 전처리에 사용된다.
3. `from sklearn.linear_model import SGDClassifier`
4. `sc_cfg = SGDClassifier(loss='log_loss', max_iter=5, random_state=42)`: 로지스틱손실함수 객체 생성
5. 학습 데이터에 로지스틱손실함수 학습시킨다.
6. 최저점을 만족하지 않을 수도 있다.


## partial_fit()
> 위의 6번에서 최저점을 만족하지 않을 때 훈련 데이터를 다시 복구시켜 에포크를 한번씩 수행하며 최저점을 탐색한다.

1. `sc_cfg.partial_fit(X_train_scl, y_train)` 반복해서 실행할 수록 테스트의 정확도가 상승한다.
   - 과대적합이 되기 전에 에포크를 반복하는 것을 멈추고 조기 종료해야 한다.
2. **조기종료**
   - 에포크를 한번씩 실행하면서 `sc_cfg.score(X_train_scl, y_train)`과 `sc_cfg.score(X_test_scl, y_test)`의 점수 사이의 간격이 가장 좁은 지점을 찾는다.